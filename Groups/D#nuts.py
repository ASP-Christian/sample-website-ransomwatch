
import time
from selenium import webdriver
import json
import datetime
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
site = 'http://sbc2zv2qnz5vubwtx3aobfpkeao6l4igjegm3xx7tk5suqhjkp5jxtqd.onion/'

driver.get(site)
time.sleep(10)

company_names = []
Data = []
company_description = []
data_date = []

while True:

    name_elements = driver.find_elements("xpath", '//div[@class="box post-box"]/h2/a')
    for element in name_elements:
        company_names.append(element.get_attribute("innerText") if element.get_attribute("innerText") else 'n/a')

    desc_elements = driver.find_elements("xpath", '//p[@class="post-excerpt"]')
    for element in desc_elements:
        company_description.append(element.get_attribute("innerText") if element.get_attribute("innerText") else 'n/a')

    Data_elements = driver.find_elements("xpath", '//div[@class="box post-box"]/h2/a')
    for element in Data_elements:
        Data.append(element.get_attribute("href") if element.get_attribute("href") else 'n/a')

    date_elements = driver.find_elements("xpath", '//span[@class="post-meta"]/time')
    for element in date_elements:
        date_str = element.get_attribute("innerText")
        if date_str:
            # Parse the date string into a datetime object
            date_obj = datetime.datetime.strptime(date_str, '%d %b %Y')
            # Format the datetime object as 'YYYY-MM-DD'
            formatted_date = date_obj.strftime('%Y-%m-%d')
            data_date.append(formatted_date)
        else:
            data_date.append('n/a')

    pagination_element = driver.find_elements("xpath", '//i[@class="icon icon-arrow-right"]')

    if not pagination_element:
        break

    driver.execute_script("arguments[0].click();", pagination_element[1])

    time.sleep(5)

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
            'ransomware_name': 'D#NUT',
            'ransomware_site': 'http://sbc2zv2qnz5vubwtx3aobfpkeao6l4igjegm3xx7tk5suqhjkp5jxtqd.onion/',
            'data_description': company_description[i],
            'data_date': data_date[i],  # Use the modified current_date
            'download_data': Data[i],
            'company_website': company_description[i],
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
