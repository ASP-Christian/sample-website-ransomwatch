from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import time
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
site = 'http://stniiomyjliimcgkvdszvgen3eaaoz55hreqqx6o77yvmpwt7gklffqd.onion'
driver.get(site)

# Wait for 10 seconds
time.sleep(5)

# Create empty lists to store the data
data_elements = driver.find_elements("xpath", '//div[@class="action"]/button')
company_names = []
urls = []
company_descriptions = []

while True:
    for data_element in data_elements:
        try:
            # Click on the data_element
            data_element.click()

            # Extract the company name
            desc_element = driver.find_element("xpath", '//div[@class="company_body"]')
            desc_name = desc_element.text
            company_descriptions.append(desc_name)

            company_element = driver.find_element("xpath", '//div[@class="company_title"]')
            company_name = company_element.text
            company_names.append(company_name)

            # Find the href element
            try:
                href_element = driver.find_element("xpath", '//iframe[@class="bastaframe"]')
                href = href_element.get_attribute("src")
            except NoSuchElementException:
                href = driver.current_url

            urls.append(href)

            # Press ESC key
            close = driver.find_element("xpath", '//div[@class="close_container"]/img')
            close.click()

        except StaleElementReferenceException:
            # Handle the exception by refreshing the data_elements
            data_elements = driver.find_elements("xpath", '//div[@class="action"]/button')
            continue

    # Check if the next page button exists
    try:
        pagination = driver.find_element("xpath", '//div[@class="next-page-btn"]')
    except NoSuchElementException:
        break  # Break the loop if the pagination does not exist

    # Click on the next page button
    pagination.click()

    # Wait for a short time for the next page to load
    time.sleep(2)

    # Update the data_elements with the new page elements
    data_elements = driver.find_elements("xpath", '//div[@class="action"]/button')

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
            'company_description': company_descriptions[i],
            'ransomware_name': 'Black Basta Blog',
            'ransomware_site': 'http://stniiomyjliimcgkvdszvgen3eaaoz55hreqqx6o77yvmpwt7gklffqd.onion',
            'data_description': company_descriptions[i],
            'data_date': current_date,  # Use the modified current_date
            'download_data': urls[i],
            'company_website': 'Website inside description',
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

