import pandas as pd

from selenium import webdriver
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
site = 'http://ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion'
driver.get(site)

Data = []
company_description = []
company_names = []

while True:
    try:
        # Extract link and description data from the current page
        data_elements = driver.find_elements("xpath", '//h2[@class="entry-title heading-size-1"]/a')
        desc_elements = driver.find_elements("xpath", '//div[@class="entry-content"]/p')

        for element in data_elements:
            Data.append(element.get_attribute("href"))
            company_names.append(element.text if element.text else 'n/a')

        for element in desc_elements:
            company_description.append(element.text if element.text else 'n/a')

        # Scroll to the pagination element using JavaScript
        pagination = driver.find_element("xpath", '//a[@class="next page-numbers"]/span[2]')

        # Click the pagination element using JavaScript
        driver.execute_script("arguments[0].click();", pagination)
        time.sleep(6)  # Add a small delay to allow the next page to load

    except:
        # If no "Next" button is found or any other error occurs, exit the loop
        break

# Get the current date and time in US Eastern Time (ET)
us_eastern_timezone = pytz.timezone('US/Eastern')
current_date_time = datetime.now(us_eastern_timezone)

# Format the current date and time as a string in ISO format
current_date = current_date_time.strftime('%Y-%m-%d ')

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
            'company_description': company_description[i],
            'ransomware_name': 'Everest Ransomware Group',
            'ransomware_site': 'http://ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion',
            'data_description': company_description[i],
            'data_date': current_date,  # Use the modified current_date
            'download_data': Data[i],
            'company_website': 'website on description',
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