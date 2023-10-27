from selenium import webdriver
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
site = 'http://rnsm777cdsjrsdlbs4v5qoeppu3px6sb2igmh53jzrx7ipcrbjz5b2ad.onion/'
driver.get(site)

# get the total number of pages
total_pages = len(driver.find_elements("xpath", '//div[@class="col-md-10"]/div/ul/li'))

# create empty lists to store the data
company_names = []
company_description = []
company_website = []
Company_Link = []
Data_Leak = []
# loop through all the pages of the website
for page in range(1, total_pages + 1):
    # update the website URL with the page number
    site_url = site + '?page=' + str(page)
    driver.get(site_url)

    # extract the data from the current page
    name_elements = driver.find_elements("xpath", '//h5[@class="card-title"]')
    for element in name_elements:
        company_names.append(element.text)

    desc_elements = driver.find_elements("xpath", '//div[@class="row justify-content-md-center"]/div/div/div/p[2]')
    for element in desc_elements:
        company_description.append(element.text)

    website_elements = driver.find_elements("xpath", '//p[@class="card-text mt-3 text-secondary"]')
    for element in website_elements:
        company_website.append(element.text.split(',')[0].replace('published: ', '').strip())

    Companylinks = driver.find_elements("xpath", '//div[@class="row justify-content-md-center"]/div/div/div/p[1]/a')
    for Companylink in Companylinks:
        Company_Link.append(Companylink.get_attribute('href'))

    Datas = driver.find_elements("xpath", '//a[@class="btn btn-outline-primary"]')
    for Data in Datas:
        Data_Leak.append(Data.get_attribute('href'))

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
            'ransomware_name': 'ransomexx2',
            'ransomware_site': 'http://rnsm777cdsjrsdlbs4v5qoeppu3px6sb2igmh53jzrx7ipcrbjz5b2ad.onion/',
            'data_description': company_description[i],
            'data_date': company_website[i],  # Use the modified current_date
            'download_data': Data_Leak[i],
            'company_website': Company_Link[i],
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
