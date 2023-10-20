
import time

from selenium import webdriver
import json
from datetime import datetime
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
site = 'http://hl66646wtlp2naoqnhattngigjp5palgqmbwixepcjyq5i534acgqyad.onion'
driver.get(site)

company_names = []
company_description = []
Data = []
date = []

while True:

    name_elements = driver.find_elements("xpath", '//div[@class="a-b-n-name"]')
    for element in name_elements:
        company_names.append(element.text if element.text else 'n/a')

    date_elements = driver.find_elements("xpath", '//div[@class="a-b-h-time"]')

    for element in date_elements:
        date_str = element.text
        if date_str:
            # Parse the original date string into a datetime object
            original_date = datetime.strptime(date_str, '%b %d, %Y %I:%M %p')

            # Format the datetime object as YYYY-MM-DD
            yyyy_mm_dd = original_date.strftime('%Y-%m-%d')
            date.append(yyyy_mm_dd)
        else:
            date.append('n/a')

    company_description_elements = driver.find_elements("xpath", "//div[@class='a-b-text']")
    for element in company_description_elements:
        company_description.append(element.text if element.text else 'n/a')

    Data_elements = driver.find_elements("xpath", '//button[@class="a-b-b-r-l-button"]')
    for element in Data_elements:
        onclick_value = element.get_attribute("onclick")
        if onclick_value:
            start_index = onclick_value.find("'") + 1
            end_index = onclick_value.find("'", start_index)
            location_value = onclick_value[start_index:end_index]
            full_url = site + "/" + location_value
            Data.append(full_url)
        else:
            Data.append('n/a')

    pagination_element = driver.find_elements("xpath", '//a[@class="m-n-n-link"]/p[contains(text(), "Next page")]')

    if not pagination_element:
        break

    driver.execute_script("arguments[0].click();", pagination_element[0])

    time.sleep(10)

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
            'ransomware_name': 'News-Snatch',
            'ransomware_site': 'http://hl66646wtlp2naoqnhattngigjp5palgqmbwixepcjyq5i534acgqyad.onion',
            'data_description': company_description[i],
            'data_date': date[i],  # Use the modified current_date
            'download_data': Data[i],
            'company_website': 'website in description',
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
