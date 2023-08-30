from selenium import webdriver
import pandas as pd
import time


# set up TOR and the TOR browser
tor_proxy = "socks5://127.0.0.1:9150"
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9150)
profile.set_preference('network.proxy.socks_remote_dns', True)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile, executable_path='/path/to/geckodriver')

# navigate to the website
site = 'http://medusaxko7jxtrojdkxo66j7ck4q5tgktf7uqsqyfry4ebnxlcbkccyd.onion/'
driver.get(site)

while True:
    # Get current page height
    current_height = driver.execute_script("return document.documentElement.scrollHeight")

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # Wait for a short time for the content to load
    time.sleep(2)

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

# extract the data from the current page
name_elements = driver.find_elements("xpath", '//div[@class="card-header"]')
for element in name_elements:
    company_names.append(element.text if element.text else 'n/a')

company_description_elements = driver.find_elements("xpath", "//div[@class='card-body']")
for element in company_description_elements:
    company_description.append(element.text if element.text else 'n/a')

Data_elements = driver.find_elements("xpath", '//div[@class="card"]')
for element in Data_elements:
    data_id = element.get_attribute("data-id")
    if data_id:
        Data.append(site + 'detail?id=' + data_id)


# Creating a pandas DataFrame
df = pd.DataFrame({
    'company': company_names,
    'company_description': company_description,
    'ransomware_name': ['Medusa Blog'] * len(company_names),
    'ransomware_site': ['http://medusaxko7jxtrojdkxo66j7ck4q5tgktf7uqsqyfry4ebnxlcbkccyd.onion/'] * len(company_names),
    'data_description': ['The data could come in various forms, such as PDFs, XLSX files, DOCX documents, CSV spreadsheets, TXT text files, JPG and PNG images, as well as MP4 and WAV audiovisual formats, among others.'] * len(company_names),
    'data_date': ['2023-01-01'] * len(company_names),
    'download_data': Data,
    'company_website': ['https://www.example.com/'] * len(company_names),
})

driver.quit()
