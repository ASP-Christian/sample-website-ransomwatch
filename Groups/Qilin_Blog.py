from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

import json
from datetime import datetime
import os
import pytz  # Import pytz

# Set the working directory to the directory where your script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Create a directory to store JSON files if it doesn't exist
datas_folder = os.path.join(script_dir, "Overall_data")
if not os.path.exists(datas_folder):
    os.mkdir(datas_folder)

# Set up TOR and the TOR browser
tor_proxy = "socks5://127.0.0.1:9150"
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = tor_proxy
proxy.ssl_proxy = tor_proxy

# Set Firefox to run in headless mode
options = webdriver.FirefoxOptions()
options.headless = True

# Create a Firefox WebDriver instance with the proxy settings and options
driver = webdriver.Firefox(options=options, proxy=proxy)

# Navigate to the website
site = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'
driver.get(site)

company_names = []
company_description = []
company_websites = []
Data = []

name_elements = driver.find_elements("xpath", '//h2[@class="post-title"]/a')
for element in name_elements:
    company_names.append(element.text if element.text else 'n/a')

company_description_elements = driver.find_elements("xpath", "//div[@class='post-des dropcap']/p")
for element in company_description_elements:
    company_description.append(element.text if element.text else 'n/a')

company_elements = driver.find_elements("xpath", '//div[@class="category-mid-post-two"]/div[1]/span/a')
for element in company_elements:
    href = element.get_attribute("href")
    if href:
        company_websites.append(href.replace('https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/', ''))
    else:
        company_websites.append('n/a')

Data_elements = driver.find_elements("xpath", '//h2[@class="post-title"]/a')
for element in Data_elements:
    Data.append(element.get_attribute("href") if element.get_attribute("href") else 'n/a')

# Get the current date and time in US Eastern Time (ET)
us_eastern_timezone = pytz.timezone('US/Eastern')
current_date_time = datetime.now(us_eastern_timezone)

# Format the current date and time as a string in ISO format
current_date = current_date_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')

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
            'ransomware_name': 'Magazine',
            'ransomware_site': 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/',
            'data_description': company_description[i],
            'data_date': current_date,  # Use the modified current_date
            'download_data': Data[i],
            'company_website': company_websites[i]
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
