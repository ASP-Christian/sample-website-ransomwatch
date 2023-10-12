from tqdm import tqdm
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
site = 'http://rgleaktxuey67yrgspmhvtnrqtgogur35lwdrup4d3igtbm3pupc4lyd.onion'
driver.get(site)


Dls_Links = driver.find_elements("xpath", '//div[@class="card"]/p/a')  # Links to visits .href

date_of_data = []
Company = []
Company_Description = []
Company_Website = []
Size_of_Data = []
Download_Leak_Data = []
DLS_Website = []
DLS_Onion_Link = []

Dates = driver.find_elements("xpath", '//div[@class="card"]/p[2]')  # Date of Data .text
for Date in Dates:
    date_of_data.append(Date.text.strip('Published: '))

Listoflink = []
for Dls_Link in Dls_Links:
    Listoflink.append(Dls_Link.get_attribute('href'))

for i in tqdm(range(len(Listoflink))):
    driver.get(Listoflink[i])
    DLS_Website.append('Ragnar_Locker Leaks site')
    DLS_Onion_Link.append('http://rgleaktxuey67yrgspmhvtnrqtgogur35lwdrup4d3igtbm3pupc4lyd.onion')
    Company.append(driver.find_element("xpath", '/html/body/div[3]/div/div[1]/div/h1').text)
    elements = driver.find_elements("xpath", '//div[@id="_tl_view"]/p')[0:5]
    text_list = [elem.text for elem in elements]
    Company_Description.append('\n'.join(text_list).strip())
    Company_Website_elements = driver.find_elements("xpath", '//a[@target="_blank"]')
    if Company_Website_elements:
        Company_Website.append(Company_Website_elements[0].get_attribute('href'))
    else:
        Company_Website.append('n/a')

    Size_of_Data_elements = driver.find_elements("xpath", '//div[@class="card"]/p[2]')
    if Size_of_Data_elements:
        Size_of_Data.append(Size_of_Data_elements[0].text)
    else:
        Size_of_Data.append('n/a')

    Download_Leak_Data_elements = driver.find_elements("xpath", '//*[@id="DOWNLOAD"]/a')
    if Download_Leak_Data_elements:
        Download_Leak_Data.append(Download_Leak_Data_elements[0].get_attribute('href'))
    elif driver.find_elements("xpath", '/html/body/div[3]/div/div[1]/div/p[5]/a'):
        Download_Leak_Data.append(
            driver.find_elements("xpath", '/html/body/div[3]/div/div[1]/div/p[5]/a')[0].get_attribute('href'))
    elif driver.find_elements("xpath", '/html/body/div[3]/div/div[1]/div/h3/a'):
        Download_Leak_Data.append(
            driver.find_elements("xpath", '/html/body/div[3]/div/div[1]/div/h3/a')[0].get_attribute('href'))
    elif driver.find_elements("xpath", '/html/body/div[3]/div/div[1]/div/figure[2]'):
        Download_Leak_Data.append(
            driver.find_elements("xpath", '/html/body/div[3]/div/div[1]/div/figure[2]')[0].get_attribute('href'))
    else:
        Download_Leak_Data.append('n/a')


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
for i in range(len(Company)):
    if Company[i] not in existing_company_names:
        data_dict = {
            'company': Company[i],
            'company_description': Company_Description[i],
            'ransomware_name': 'Ragnar Locker',
            'ransomware_site': 'http://rgleaktxuey67yrgspmhvtnrqtgogur35lwdrup4d3igtbm3pupc4lyd.onion',
            'data_description': Company_Description[i],
            'data_date': current_date,  # Use the modified current_date
            'download_data': Listoflink[i],
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
