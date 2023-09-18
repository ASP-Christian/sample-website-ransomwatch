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
options.headless = True  # Change to True or False as needed

# Create a Firefox WebDriver instance with the options
driver = webdriver.Firefox(options=options)

# Wait for the Tor service to be ready
while True:
    try:
        driver.get("https://check.torproject.org/")
        if "Congratulations. This browser is configured to use Tor." in driver.page_source:
            break
        else:
            time.sleep(5)  # Wait for a few seconds before checking again
    except Exception as e:
        print(f"Error checking Tor status: {e}")
        time.sleep(5)  # Wait for a few seconds before checking again

# Navigate to the website
site = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'
driver.get(site)

print("Success Success Success Success")