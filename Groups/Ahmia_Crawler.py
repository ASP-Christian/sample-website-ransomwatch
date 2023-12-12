import os
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
from datetime import datetime
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

# List of onion links
onion_links = [
    "http://ssq4zimieeanazkzc5ld4v5hdibi2nzwzdibfh5n5w4pw5mcik76lzyd.onion",
    "http://ml3mjpuhnmse4kjij7ggupenw34755y4uj7t742qf7jg5impt5ulhkid.onion",
    "http://vsociethok6sbprvevl4dlwbqrzyhxcxaqpvcqt5belwvsuxaxsutyad.onion",
    "http://wmp2rvrkecyx72i3x7ejhyd3yr6fn5uqo7wfus7cz7qnwr6uzhcbrwad.onion",
    "http://invest3ulzmkaq2vuz63rwt2brb3d2gndlvpbpzg2gwko7buwllkigyd.onion",
    "http://bpynhpfpdydv6axdm2xeu6y6cbzed73aztxdjyq5gygblzt6v2zjegid.onion",
]

# Get the current date in the format (year, month, day)
current_date = datetime.now().strftime("%Y-%m-%d")

# Iterate through the onion links
for group_url in onion_links:
    title = ""
    status_code = 404
    is_active = False

    try:
        renew_tor_ip()
        response = requests.get(group_url, proxies=tor_proxy, verify=False)

        status_code = response.status_code

        if 200 <= status_code < 300:
            is_active = True

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()

        print(f"Group URL: {group_url}\nTitle: {title}\nStatus Code: {status_code}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error for {group_url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {group_url}: {str(e)}")

    print("-----")
