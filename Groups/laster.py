import os
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time  # Import the time module

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
index_file = 'Groups/Overall_data/index_group.json'  # Existing index file

try:
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Initialize a list to store the group data
    group_data = []

    for group_entry in data:
        group_url = group_entry.get('group')

        # Initialize default values
        title = ""
        status_code = None  # Default status code is None
        is_active = False

        # Send a request through the TOR proxy with certificate verification disabled
        try:
            renew_tor_ip()  # Renew TOR IP address before making the request
            response = requests.get(group_url, proxies=tor_proxy, verify=False, timeout=30)  # Adjust timeout as needed

            # Get the status code
            status_code = response.status_code

            # Determine if the website is active based on status code
            if 200 <= status_code < 300:
                is_active = True

            # Parse the HTML content if the status code is valid
            if is_active:
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

        # Sleep for a few seconds to avoid overloading the TOR network
        time.sleep(2)

    # Load the existing index data
    try:
        with open(index_file, 'r') as existing_file:
            existing_data = json.load(existing_file)
    except FileNotFoundError:
        existing_data = []

    # Get the current date in the format (year, month, day)
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Update existing data based on Group_url or add new entries
    for new_item in group_data:
        updated = False
        for item in existing_data:
            if item['group_url'] == new_item['group_url']:
                item['date'] = current_date
                item['status_code'] = new_item['status_code']
                item['title'] = new_item['title']
                item['is_active'] = new_item['is_active']
                updated = True
                break
        if not updated:
            new_item['date'] = current_date
            existing_data.append(new_item)

    # Save the combined data to the index file
    with open(index_file, 'w') as output_file:
        json.dump(existing_data, output_file, indent=4)

    print("Data collected and updated in 'index_group.json'.")

except FileNotFoundError:
    print(f"File '{json_file}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
