import os
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
import json
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

# .onion URL to scrape
onion_url = 'http://lorenzmlwpzgxq736jzseuterytjueszsvznuibanxomlpkyxk6ksoyd.onion'

# Set the headers to use Tor proxy
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

# Renew Tor IP address before making the request
renew_tor_ip()

try:
    # Make a request using Tor proxy
    response = requests.get(onion_url, proxies=tor_proxy, headers=headers)

    # Check the status code
    status_code = response.status_code

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and print the title
    title = soup.title.string if soup.title else 'Title not found'
    print(f'Title: {title}')

    # Print the status code
    print(f'Status Code: {status_code}')

except Exception as e:
    print(f'Error: {e}')

