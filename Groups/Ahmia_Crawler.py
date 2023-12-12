import requests
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

# URL to check
group_url = 'ssq4zimieeanazkzc5ld4v5hdibi2nzwzdibfh5n5w4pw5mcik76lzyd.onion/'

try:
    renew_tor_ip()
    response = requests.get(group_url, proxies=tor_proxy, verify=False)

    status_code = response.status_code
    print(f"Status code for {group_url}: {status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error for {group_url}: {e}")
except Exception as e:
    print(f"An unexpected error occurred for {group_url}: {str(e)}")
