import os
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
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

# Load the JSON data from the file
json_file = 'Groups/Overall_data/small_sample.json'

try:
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Initialize a list to store the group data
    group_data = []

    for group_entry in data:
        group_url = group_entry.get('group')

        # Initialize default values
        title = ""
        status_code = 404  # Default status code
        is_active = False

        # Send a request through the TOR proxy with certificate verification disabled
        try:
            renew_tor_ip()  # Renew TOR IP address before making the request
            response = requests.get(group_url, proxies=tor_proxy, verify=False)

            # Get the status code
            status_code = response.status_code

            # Determine if the website is active based on status code
            if 200 <= status_code < 300:
                is_active = True

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Get the title of the website
            title = soup.title.string.strip()

        except requests.exceptions.RequestException as e:
            print(f"Error for {group_url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {group_url}: {str(e)}")

        # Store group data in a dictionary
        group_info = {
            'group_url': group_url,
            'title': title,
            'status_code': status_code,
            'is_active': is_active
        }

        # Append the group data to the list
        group_data.append(group_info)

    # Save the collected data to a JSON file
    with open('Groups/Overall_data/collected_data.json', 'w') as output_file:
        json.dump(group_data, output_file, indent=4)

    print("Data collected and saved in 'collected_data.json'.")

except FileNotFoundError:
    print(f"File '{json_file}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
