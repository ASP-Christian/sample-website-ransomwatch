from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
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
options = Options()
options.add_argument('-headless')
options.add_argument(f'-proxy-server={tor_proxy}')

# Set up the WebDriver with GeckoDriver
geckodriver_path = "/snap/bin/geckodriver"
service = FirefoxService(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

# Wait for Tor to establish a connection
time.sleep(5)

# Navigate to the website
site = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'
driver.get(site)
print('Christian Algordo')
# Rest of your script remains the same
# ...

# Close the driver
driver.quit()
