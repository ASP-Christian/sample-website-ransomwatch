from selenium import webdriver
import pandas as pd
import time
from selenium import webdriver
import json
from datetime import datetime
import os
import pytz

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
site = 'http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion/'
driver.get(site)
time.sleep(10)

company_names = []
date = []
Data = []
desc = []

name_elements = driver.find_elements("xpath", '//div[@class="blog-post-content"]/a/h2')
for element in name_elements:
    company_names.append(element.get_attribute("innerText") if element.get_attribute("innerText") else 'n/a')

date_elements = driver.find_elements("xpath", '//div[@class="blog-post-meta"]/p')
for element in date_elements:
    date.append(element.get_attribute("innerText") if element.get_attribute("innerText") else 'n/a')

desc_elements = driver.find_elements("xpath", '//div[@class="blog-post-content"]/p')
for element in desc_elements:
    desc.append(element.get_attribute("innerText") if element.get_attribute("innerText") else 'n/a')

Data_elements = driver.find_elements("xpath", '//div[@class="blog-post-content"]/a[2]')
for element in Data_elements:
    Data.append(element.get_attribute("href") if element.get_attribute("href") else 'n/a')

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
            'company_description': desc[i],
            'ransomware_name': 'Quantum Blog',
            'ransomware_site': 'http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion/',
            'data_description': desc[i],
            'data_date': date[i],  # Use the modified current_date
            'download_data': Data[i],
            'company_website': 'Not Available',
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


