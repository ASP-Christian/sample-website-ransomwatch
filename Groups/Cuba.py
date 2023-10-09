from selenium import webdriver
import pandas as pd
import time
from tqdm import tqdm
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
site = 'http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/'
driver.get(site)

while True:
    try:
        next_button = driver.find_element("xpath", '/html/body/div[2]/div/div/div[1]/div[2]/div/div/button')
        next_button.click()
        time.sleep(1)  # adjust the delay between clicks as needed
    except:
        # print("Button not clickable anymore")
        break

Listoflink = []
Dls_Links = driver.find_elements("xpath", '//div[@class="list-text"]/a')
for Dls_Link in Dls_Links:
    Listoflink.append(Dls_Link.get_attribute('href'))

Listoflink = []
Dls_Links = driver.find_elements("xpath", '//div[@class="list-text"]/a')
for Dls_Link in Dls_Links:
    Listoflink.append(Dls_Link.get_attribute('href'))

Company_Name = []
Company_Desc = []
Date_Publish = []
Company_Website = []
Download_Data = []


for i in tqdm(range(len(Listoflink))):
    driver.get(Listoflink[i])
    DLS_Website = 'Cuba RANSOMWARE'
    DLS_Onion_Link = 'http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/'

    company_name = driver.find_elements("xpath", '/html/body/div/div/div[2]/div[1]')
    company_name = company_name[0].text if company_name else 'n/a'
    Company_Name.append(company_name)

    company_desc = driver.find_elements("xpath", '//div[@class="page-list-right"]/p')
    if company_desc:
        company_desc = company_desc[0].text
    elif driver.find_elements("xpath", '//div[@class="page-list-span"]'):
        company_desc = driver.find_elements("xpath", '//div[@class="page-list-span"]')[0].text
    else:
        company_desc = 'n/a'
    Company_Desc.append(company_desc)

    company_website = driver.find_elements("xpath", '//div[@class="page-list-right"]/p[4]')
    if company_website:
        company_website = company_website[0].text.strip('website: ')
    elif driver.find_elements("xpath", '//div[@class="page-list-ul"]/p[2]'):
        company_website = driver.find_elements("xpath", '//div[@class="page-list-ul"]/p[2]')[0].text.strip('website: ')
    else:
        company_website = 'n/a'
    Company_Website.append(company_website)

    data_desc = driver.find_elements("xpath", '//div[@class="page-list-right"]/p[5]')
    if data_desc:
        data_desc = data_desc[0].text.strip('files: ')
    elif driver.find_elements("xpath", '//div[@class="page-list-ul"]/p[3]'):
        data_desc = driver.find_elements("xpath", '//div[@class="page-list-ul"]/p[3]')[0].text.strip('files: ')
    else:
        data_desc = 'n/a'
    Download_Data.append(data_desc)

    date_publish = driver.find_elements("xpath", '//div[@class="page-list-right"]/p[3]')
    if date_publish:
        date_publish = date_publish[0].text.strip('Date the files were received: ')
    elif driver.find_elements("xpath", '//div[@class="page-list-ul"]/p[1]'):
        date_publish = driver.find_elements("xpath", '//div[@class="page-list-ul"]/p[1]')[0].text.strip(
            'Date the files were received: ')
    else:
        date_publish = 'n/a'
    Date_Publish.append(date_publish)

    download_data = driver.find_elements("xpath", '//div[@class="page-list-download"]/a')
    download_data = download_data[0].get_attribute('href') if download_data else 'n/a'
    Download_Data.append(download_data)

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
for i in range(len(Company_Name)):
    if Company_Name[i] not in existing_company_names:
        data_dict = {
            'company': Company_Name[i],
            'company_description': Company_Desc[i],
            'ransomware_name': 'Cuba',
            'ransomware_site': 'http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/',
            'data_description': Company_Desc[i],
            'data_date': current_date,  # Use the modified current_date
            'download_data': Download_Data[i],
            'company_website': Company_Website[i],
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
