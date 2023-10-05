from selenium import webdriver
import json
from datetime import datetime
import os
import pytz
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
site = 'http://jbeg2dct2zhku6c2vwnpxtm2psnjo2xnqvvpoiiwr5hxnc6wrp3uhnad.onion'
driver.get(site)

# create an empty list to store the Company Names
company_names = []
company_description = []
Company_Website = []
Data_Leaks_Link = []
dls_descriptions = []
dls_websites = []
dls_links = []
data_leak_dates = []
# loop through all the pages of the website
while True:
    # wait for the page to load
    time.sleep(10)

    # extract the Company Names from the current page
    ##company_name_elements = driver.find_elements_by_css_selector('h1.target-name')
    company_name_elements = driver.find_elements("xpath",
                                                 '//table[@class="table table-bordered table-content "][1]//td/h1')
    for element in company_name_elements:
        company_names.append(element.text)

    descs = driver.find_elements("xpath", '//table[@class="table table-bordered table-content "][1]//td/div/p')
    for dec in descs:
        company_description.append(dec.text)

    Webs = driver.find_elements("xpath", '//div[@class="col-sm-4"]/a')
    for Web in Webs:
        Company_Website.append(Web.get_attribute('href'))

    # Dinfos = driver.find_elements("xpath", '//div[@class="info-column"][1]')
    # for Dinfo in Dinfos:
    # DLS_Description.append(Dinfo.text)

    Dinfos = driver.find_elements("xpath", '//div[@class="info-column"]')
    for Dinfo in Dinfos:
        dls_descriptions.append(Dinfo.get_attribute('innerText'))
        dls_websites.append('BB Auction')
        dls_links.append('http://jbeg2dct2zhku6c2vwnpxtm2psnjo2xnqvvpoiiwr5hxnc6wrp3uhnad.onion')
        data_leak_dates.append('04/03/2023')

    Dls1s = driver.find_elements("xpath", '//div[@class="col-6 col-md-4"]//a[@href]')
    for Dls1 in Dls1s:
        Data_Leaks_Link.append(Dls1.get_attribute('href'))

    # find the "Next" button and click it to go to the next page
    try:
        next_button = driver.find_element("xpath", '//li[@class="page-item next" ]/a')
        next_button.click()
    except:
        # if there's no "Next" button, we've reached the last page
        break


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
            'ransomware_name': 'BB Auction',
            'ransomware_site': 'http://jbeg2dct2zhku6c2vwnpxtm2psnjo2xnqvvpoiiwr5hxnc6wrp3uhnad.onion',
            'data_description': company_description[i],
            'data_date': data_leak_dates[i],  # Use the modified current_date
            'download_data': Data_Leaks_Link[i],
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