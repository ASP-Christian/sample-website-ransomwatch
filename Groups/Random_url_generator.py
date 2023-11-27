import random
import string
import json
import requests
import socks
import socket
from requests.exceptions import ConnectionError
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
from datetime import datetime

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

def check_active(link):
    try:
        renew_tor_ip()
        response = requests.get(link, proxies=tor_proxy, verify=False, timeout=5)

        status_code = response.status_code

        if 200 <= status_code < 300:
            return True  # Link is active
        else:
            print(f"Unexpected status code {status_code} for {link}")
            print(response.text)  # Print response content for debugging
            print(response.headers)  # Print response headers for debugging

    except requests.exceptions.RequestException as e:
        print(f"Error for {link}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {link}: {str(e)}")
    return False  # Link is not active

# Function to test a list of URLs
def test_urls(urls):
    for url in urls:
        is_active = check_active(url)
        status = "Success" if is_active else "Not Active"
        print(f"{url}: {status}")

# Test URLs
test_urls = [
    "http://5n4qdkw2wavc55peppyrelmb2rgsx7ohcb2tkxhub2gyfurxulfyd3id.onion/",
    "http://12323332ub2gyfurxulfyd3id.onion/"
]
