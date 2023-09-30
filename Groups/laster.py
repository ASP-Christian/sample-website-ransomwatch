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
    current_date = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

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

        # Search for a matching entry in existing_data based on "ransomware_site"
        matching_entry = next((item for item in existing_data if 'ransomware_site' in item and item['ransomware_site'] == group_url), None)

        if matching_entry:
            # Only update the entry if incoming "is_active" is True or if the existing entry has "is_active" as True
            if is_active or matching_entry.get('is_active', False):
                matching_entry['group_url'] = group_url
                matching_entry['title'] = title
                matching_entry['status_code'] = status_code
                matching_entry['is_active'] = is_active
                matching_entry['date'] = current_date
        else:
            # If no match is found, create a new entry with the required keys and "is_active" as True
            new_item = {
                'company': group_entry.get('company', ""),
                'company_description': group_entry.get('company_description', ""),
                'ransomware_name': group_entry.get('ransomware_name', ""),
                'ransomware_site': group_url,
                'data_description': group_entry.get('data_description', ""),
                'data_date': group_entry.get('data_date', ""),
                'download_data': group_entry.get('download_data', ""),
                'company_website': group_entry.get('company_website', ""),
                'group_url': group_url,
                'title': title,
                'status_code': status_code,
                'is_active': is_active,
                'date': current_date,
            }
            existing_data.append(new_item)

    # Save the updated data to the index file
    with open(index_file, 'w') as output_file:
        json.dump(existing_data, output_file, indent=4)

    print("Data collected and updated in 'data_post.json'.")

except FileNotFoundError:
    print(f"File '{json_file}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
