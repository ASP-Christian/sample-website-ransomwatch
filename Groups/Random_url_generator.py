import random
import string
import json
import requests
import socks
import socket
from requests.exceptions import RequestException
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
            soup = BeautifulSoup(response.content, 'html.parser')
            # Add your BeautifulSoup parsing logic here

            # For demonstration, let's print the title of the page
            title = soup.title.string.strip()
            print(f"{link}: Status Code {status_code}, Title: {title}")

            return status_code  # Return status code if link is active

    except RequestException as e:
        print(f"Error for {link}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {link}: {str(e)}")
    
    return None  # Return None if link is not active or an error occurred

# Test URLs
test_urls = [
    "http://5n4qdkw2wavc55peppyrelmb2rgsx7ohcb2tkxhub2gyfurxulfyd3id.onion/",
    "http://12323332ub2gyfurxulfyd3id.onion/"
]

# Check status for each test URL
for url in test_urls:
    check_active(url)
