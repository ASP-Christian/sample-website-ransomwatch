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


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    starting_urls = [data['ransomware_site'] for data in load_json('Groups/Overall_data/data1_post.json')]
    max_crawl_depth = 4

    results = []
    for starting_url in starting_urls:
        renew_tor_ip()  # Renew Tor IP before starting
        discovered_websites = crawl_with_tor(starting_url, max_depth=max_crawl_depth)

        group_info = {
            "group_url": starting_url,
            "title": [data['ransomware_name'] for data in load_json('Groups/Overall_data/data1_post.json') if
                      data['ransomware_site'] == starting_url][0]
        }

        for i, website in enumerate(discovered_websites, start=1):
            group_info[f"Discovered website {i}"] = website

        results.append(group_info)

    crawled_data = load_json('Groups/Overall_data/crawled.json')

    for group_info in results:
        group_url = group_info["group_url"]
        title = group_info["title"]

        if not any(entry["group_url"] == group_url and entry["title"] == title for entry in crawled_data):
            crawled_data.append(group_info)

    save_json('Groups/Overall_data/crawled.json', crawled_data)

    print("Crawling and updating crawled.json completed.")
