from selenium import webdriver
import pandas as pd
import time
from datetime import datetime
import os
import pytz
import json

# Set the working directory to the directory where your script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Create a directory to store JSON files if it doesn't exist
datas_folder = os.path.join(script_dir, "Overall_data")
if not os.path.exists(datas_folder):
    os.mkdir(datas_folder)

# Set up TOR and the TOR browser
tor_proxy = "socks5://127.0.0.1:9150"
options = webdriver.FirefoxOptions()
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '127.0.0.1')
options.set_preference('network.proxy.socks_port', 9150)
options.set_preference('network.proxy.socks_remote_dns', True)

# Set the WebDriver to run in headless mode
#options.headless = False
# options.headless = True
# Set the WebDriver to run in headless mode
options.add_argument('-headless')

# Create a Firefox WebDriver instance with the options
driver = webdriver.Firefox(options=options)
# Navigate to the website
# navigate to the website
site = 'http://zohlm7ahjwegcedoz7lrdrti7bvpofymcayotp744qhx6gjmxbuo2yid.onion/'
driver.get(site)
time.sleep(5)

company_names = []
date = []
company_websites = []
Data = []

name_elements = driver.find_elements("xpath", '//div[@class="cls_recordTop"]/p')
for element in name_elements:
    company_names.append(element.get_attribute("innerText") if element.get_attribute("innerText") else 'n/a')

Data_elements = driver.find_elements("xpath", '//div[@class="cls_record"]/a')
for element in Data_elements:
    Data.append(element.get_attribute("href") if element.get_attribute("href") else 'n/a')
name_elements = driver.find_elements("xpath", '//div[@class="cls_record"]/div[2]/div[4]/div[2]')
current_date = datetime.now().strftime('%Y-%m-%d')  # Get the current date

for element in name_elements:
    date_text = element.get_attribute("innerText")
    if date_text:
        try:
            # Convert 'DD/MM/YYYY' to 'YYYY-MM-DD'
            date_obj = datetime.strptime(date_text, '%d/%m/%Y')
            formatted_date = date_obj.strftime('%Y-%m-%d')
            date.append(formatted_date)
        except ValueError:
            date.append(current_date)  # Use the current date for invalid dates
    else:
        date.append(current_date)  # Use the current date when the date is 'n/a'



dd = driver.find_elements("xpath", '//div[@class="cls_recordMiddle"]/p')
for element in dd:
    company_websites.append(element.get_attribute("innerText") if element.get_attribute("innerText") else 'n/a')

# Load existing data from the JSON file if it exists
json_file_path = os.path.join(datas_folder, 'data_post.json')
existing_data = []
if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        existing_data = json.load(json_file)

# Create a set of existing company names for efficient lookup
existing_company_names = set(entry['company'] for entry in existing_data)

# Create a list of new entries to add to the data
new_entries = []
for i in range(len(company_names)):
    if company_names[i] not in existing_company_names:
        data_dict = {
            'company': company_names[i],
            'company_description': 'Not available',
            'ransomware_name': 'RansomHouse',
            'ransomware_site': 'http://zohlm7ahjwegcedoz7lrdrti7bvpofymcayotp744qhx6gjmxbuo2yid.onion/',
            'data_description': 'Not available',
            'data_date': date[i],  # Use the modified current_date
            'download_data': Data[i],
            'company_website': company_websites[i],
            "group_url": "1",
            "title": "1",
            "status_code": 1,
            "is_active": False,
            "date": "2023-09-30"
        }
        new_entries.append(data_dict)

# Append new entries to the existing data
existing_data.extend(new_entries)

# Save the updated data as JSON in the 'Overall_data' folder
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

print(f"Data saved to {json_file_path}")
print(new_entries)
# Close the browser
driver.quit()
