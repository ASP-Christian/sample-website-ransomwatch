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

# Send a request through the TOR proxy with certificate verification disabled
try:
    renew_tor_ip()  # Renew TOR IP address before making the request
    response = requests.get(url, proxies=tor_proxy, verify=False)
    response.raise_for_status()

    # Get the status code
    status_code = response.status_code

    # Determine if the website is active based on status code
    if 200 <= status_code < 300:
        is_active = True
    else:
        is_active = False

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the title of the website
    title = soup.title.string.strip()
    print("Website Title:", title)

    # Print the status code and whether the website is active
    print("Status Code:", status_code)
    print("Is Active:", is_active)

except requests.exceptions.RequestException as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", str(e))
