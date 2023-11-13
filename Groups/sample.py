import os
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

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

if __name__ == "__main__":
    starting_url = "http://mblogci3rudehaagbryjznltdp33ojwzkq6hn2pckvjq33rycmzczpid.onion/"
    max_crawl_depth = 1

    renew_tor_ip()  # Renew Tor IP before starting
    discovered_websites = crawl_with_tor(starting_url, max_depth=max_crawl_depth)

    print("Discovered Websites:")
    for website in discovered_websites:
        print(website)
