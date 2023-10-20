
import time

from selenium import webdriver
import json

import os


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
site = 'http://medusaxko7jxtrojdkxo66j7ck4q5tgktf7uqsqyfry4ebnxlcbkccyd.onion/'
driver.get(site)

while True:
    # Get current page height
    current_height = driver.execute_script("return document.documentElement.scrollHeight")

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # Wait for a short time for the content to load
    time.sleep(7)

    # Get new page height after scrolling
    new_height = driver.execute_script("return document.documentElement.scrollHeight")

    # Break the loop if the page height remains the same (reached the bottom)
    if new_height == current_height:
        break

company_names = []
# extract the data from the current page
name_elements = driver.find_elements("xpath", '//div[@class="card-header"]')
for element in name_elements:
    company_names.append(element.text if element.text else 'n/a')

company_names = []
company_description = []
Data = []
data_date = []

# extract the data from the current page
name_elements = driver.find_elements("xpath", '//div[@class="card-header"]')
for element in name_elements:
    company_names.append(element.text if element.text else 'n/a')

company_description_elements = driver.find_elements("xpath", "//div[@class='card-body']")
for element in company_description_elements:
    company_description.append(element.text if element.text else 'n/a')

date_elements = driver.find_elements("xpath", '//div[@class="date-updated"]/span')
for element in date_elements:
    date_string = element.text
    if date_string:
        # Split the date string and keep only the first part (YYYY-MM-DD)
        date_parts = date_string.split(' ')
        if len(date_parts) > 0:
            data_date.append(date_parts[0])
        else:
            data_date.append('n/a')
    else:
        data_date.append('n/a')

Data_elements = driver.find_elements("xpath", '//div[@class="card"]')
for element in Data_elements:
    data_id = element.get_attribute("data-id")
    if data_id:
        Data.append(site + 'detail?id=' + data_id)

json_file_path = os.path.join(datas_folder, 'data_post.json')
existing_data = []
if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        existing_data = json.load(json_file)

# Create a set of existing company names for efficient lookup
existing_company_names = set(entry['company'] for entry in existing_data)

print(len(Data))
print(len(company_names))
# Create a list of new entries to add to the data
new_entries = []
for i in range(len(company_names)):
    if company_names[i] not in existing_company_names:
        data_dict = {
            'company': company_names[i],
            'company_description': company_description[i],
            'ransomware_name': 'Medusa Blog',
            'ransomware_site': 'http://medusaxko7jxtrojdkxo66j7ck4q5tgktf7uqsqyfry4ebnxlcbkccyd.onion/',
            'data_description': company_description[i],
            'data_date': data_date[i],  # Use the modified current_date
            'download_data': Data[i],
            'company_website': 'Website in Description ',
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



