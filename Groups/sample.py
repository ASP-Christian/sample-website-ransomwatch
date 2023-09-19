import os
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup

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

# URL of the onion website
url = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'

# Send a request through the TOR proxy
try:
    renew_tor_ip()  # Renew TOR IP address before making the request
    response = requests.get(url, proxies=tor_proxy)
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the title of the website
    title = soup.title.string.strip()
    print("Website Title:", title)

except Exception as e:
    print("Error:", str(e))
