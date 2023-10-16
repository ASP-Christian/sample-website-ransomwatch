from selenium import webdriver
import json
from datetime import datetime
import os
import time

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
site = 'http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion'
driver.get(site)

time.sleep(20)

company_names = []
Data = []
company_description = []
data_date = []
company_websites = ["website N/A"]

start_time = time.time()

while True:
    name_elements = driver.find_elements("xpath", '//div[@class="post-header"]')
    for element in name_elements:
        company_names.append(element.text if element.text else 'n/a')

    name_elements = driver.find_elements("xpath", '//div[@class="post-description"]')
    for element in name_elements:
        company_description.append(element.text if element.text else 'n/a')

    name_elements = driver.find_elements("xpath", '//div[@class="post-subheader small"][1]')
    for element in name_elements:
        if element.text:
            # Parse the date in the original format
            original_date = datetime.strptime(element.text, '%a %b %d %Y')
            # Convert it to the desired format
            formatted_date = original_date.strftime('%Y-%m-%d')
            data_date.append(formatted_date)
        else:
            data_date.append('n/a')

    Data_elements = driver.find_elements("xpath", "//div[@class='post-footer-right']/a")
    for element in Data_elements:
        href = element.get_attribute("href")
        Data.append(href)

    pagination_elements = driver.find_elements("xpath", '//li[@class="bx--pagination-nav__list-item"]/button')
    if len(pagination_elements) < 2 or not pagination_elements[-1].is_enabled():
        # Break the loop if there are no more pages to navigate to or if the last pagination button is disabled
        break

    pagination = pagination_elements[-1]
    pagination.click()
    time.sleep(10)

# Load existing data from the JSON file if it exists
json_file_path = os.path.join(datas_folder, 'data_post.json')
existing_data = []
if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        existing_data = json.load(json_file)

# Create a set of existing company names for efficient lookup
existing_company_names = set(entry['company'] for entry in existing_data)

new_entries = []
for i in range(len(company_names)):
    if company_names[i] not in existing_company_names:

        data_dict = {
            'company': company_names,
            'company_description': company_description,
            'ransomware_name': 'ALPHV',
            'ransomware_site': 'http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion',
            'data_description': company_description,
            'data_date': data_date,
            'download_data': Data,
            'company_website': company_websites,
            "group_url": "1",
            "title": "1",
            "status_code": 1,
            "is_active": False,
            "date": "2023-09-30"
        }
        new_entries.append(data_dict)

# Load existing data from the JSON file if it exists
json_file_path = 'data_post.json'
existing_data = []
if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        existing_data = json.load(json_file)

# Append new entries to the existing data
existing_data.extend(new_entries)

# Save the updated data as JSON in the 'Overall_data' folder
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

print(f"Data saved to {json_file_path}")
print(new_entries)
# Close the browser
driver.quit()
