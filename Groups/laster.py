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
index_file = 'Groups/Overall_data/data_post.json'  # Updated index file path

try:
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Load the existing index data or create an empty list if it doesn't exist
    try:
        with open(index_file, 'r') as existing_file:
            existing_data = json.load(existing_file)
    except FileNotFoundError:
        existing_data = []

    # Get the current date in the format (year, month, day)
    current_date = datetime.now().strftime("%Y-%m-%d-%H")

    # Iterate through the data and update existing entries based on ransomware_site
    for group_entry in data:
        ransomware_site = group_entry.get('ransomware_site')
        group_url = group_entry.get('group')

        # Find the existing entry with a matching ransomware_site
        matching_entry = next((item for item in existing_data if item['ransomware_site'] == ransomware_site), None)

        if matching_entry:
            # Update the existing entry
            matching_entry['date'] = current_date
            matching_entry['is_active'] = True  # Set is_active to True
            matching_entry['title'] = ""
            matching_entry['status_code'] = 404

        else:
            # Create a new entry if no match is found
            new_entry = {
                'company': group_entry.get('company'),
                'company_description': group_entry.get('company_description'),
                'ransomware_name': group_entry.get('ransomware_name'),
                'ransomware_site': ransomware_site,
                'data_description': group_entry.get('data_description'),
                'data_date': group_entry.get('data_date'),
                'download_data': group_entry.get('download_data'),
                'group_url': group_url,
                'title': "",
                'status_code': 404,
                'is_active': True,
                'date': current_date
            }
            existing_data.append(new_entry)

    # Save the updated data to the index file
    with open(index_file, 'w') as output_file:
        json.dump(existing_data, output_file, indent=4)

    print("Data collected and updated in 'data_post.json'.")

except FileNotFoundError:
    print(f"File '{json_file}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
