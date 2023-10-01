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

# Load the JSON data from the file
json_file = 'Groups/Overall_data/small_sample.json'
index_file = 'Groups/Overall_data/data_post.json'  # Updated index file

try:
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Load the existing index data
    try:
        with open(index_file, 'r') as existing_file:
            existing_data = json.load(existing_file)
    except FileNotFoundError:
        existing_data = []

    # Get the current date in the format (year, month, day)
    current_date = datetime.now().strftime("%Y-%m-%d-%H,%M,%S")

    # Create a set to store the "ransomware_site" values from existing_data for faster lookups
    existing_ransomware_sites = {item.get('ransomware_site', '') for item in existing_data}

    # Iterate through the data from small_sample.json
    for group_entry in data:
        group_url = group_entry.get('group')
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

        except requests.exceptions.RequestException as e:
            print(f"Error for {group_url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {group_url}: {str(e)}")

        # Check if the "ransomware_site" exists in existing_data
        matching_entries = [item for item in existing_data if item.get('ransomware_site', '') == group_url]

        # Update all matching entries
        for matching_entry in matching_entries:
            matching_entry['group_url'] = group_url
            matching_entry['title'] = title
            matching_entry['status_code'] = status_code
            matching_entry['is_active'] = is_active
            matching_entry['date'] = current_date

    # Save the updated data to the index file
    with open(index_file, 'w') as output_file:
        json.dump(existing_data, output_file, indent=4)

    print("Data collected and updated in 'data_post.json'.")

except FileNotFoundError:
    print(f"File '{json_file}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
