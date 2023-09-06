from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
import os
import time
from selenium.common.exceptions import WebDriverException

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
options.headless = True
options.add_argument(f'-proxy-server={tor_proxy}')

# Set up the WebDriver with GeckoDriver
geckodriver_path = "/snap/bin/geckodriver"  # Update to the correct path
service = FirefoxService(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

# Wait for Tor to establish a connection (increase sleep time if needed)
time.sleep(10)

# Navigate to the website
site = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'
driver.get(site)

print("DONE SUCCESS")
