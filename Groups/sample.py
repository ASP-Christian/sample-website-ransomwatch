import os
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json

# Function to renew the TOR IP address
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="YOUR_TOR_PASSWORD")
        controller.signal(Signal.NEWNYM)

# TOR proxy settings
tor_proxy = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050',
}

def crawl_with_tor(url, max_depth=2, current_depth=0, discovered=set()):
    if current_depth > max_depth:
        return discovered

    try:
        response = requests.get(url, proxies=tor_proxy)
        if response.status_code == 200:
            discovered.add(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            links = [urljoin(url, link.get('href')) for link in soup.find_all('a')]

            for link in links:
                if link not in discovered and is_internal_link(url, link):
                    discovered = crawl_with_tor(link, max_depth, current_depth + 1, discovered)

    except Exception as e:
        print(f"Error crawling {url}: {e}")

    return discovered

def is_internal_link(base_url, link):
    base_domain = urlparse(base_url).netloc
    link_domain = urlparse(link).netloc
    return base_domain == link_domain

def count_unique_group_urls(json_data):
    unique_group_urls = set(item['group_url'] for item in json_data)
    return len(unique_group_urls)

def save_to_crawled_json(crawled_data):
    with open('Groups/Overall_data/crawled.json', 'w', encoding='utf-8') as json_file:
        json.dump(crawled_data, json_file, indent=2)

if __name__ == "__main__":
    # Read starting URLs from data_post.json
    with open('Groups/Overall_data/data_post.json', 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    # Count unique group URLs
    unique_group_url_count = count_unique_group_urls(json_data)
    print(f"Unique Group URL Count: {unique_group_url_count}")

    # Initialize crawled data
    crawled_data = []

    # Iterate through each starting URL
    for item in json_data:
        starting_url = item['group_url']
        title = item['title']

        # Renew Tor IP before starting for each URL
        renew_tor_ip()

        # Crawl and get discovered websites
        max_crawl_depth = 4
        discovered_websites = crawl_with_tor(starting_url, max_depth=max_crawl_depth)

        # Filter out discovered websites present in 'download_data'
        filtered_discovered_websites = [website for website in discovered_websites
                                        if website not in item.get('download_data', '')]

        # Create a dictionary for the crawled JSON
        crawled_entry = {
            'group_url': starting_url,
            'title': title,
        }

        # Add discovered websites to the dictionary
        for i, website in enumerate(filtered_discovered_websites, start=1):
            crawled_entry[f'Discovered website {i}'] = website

        # Append the dictionary to the list
        crawled_data.append(crawled_entry)

    # Save the crawled data to crawled.json
    save_to_crawled_json(crawled_data)

    print("Crawled data has been saved to crawled.json")
