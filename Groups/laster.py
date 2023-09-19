import os
from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# Function to renew the TOR IP address
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="YOUR_TOR_PASSWORD")
        controller.signal(Signal.NEWNYM)

# TOR proxy settings for Firefox
tor_proxy = {
    'proxyType': "manual",
    'socksProxy': "localhost:9050",
    'socksVersion': 5,
}

# URL of the onion website
url = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'

# Configure Firefox to use TOR proxy settings in headless mode
firefox_options = Options()
firefox_options.headless = True
firefox_options.add_argument('--proxy-server=socks5://localhost:9050')

# Start Firefox with TOR settings
driver = webdriver.Firefox(options=firefox_options)

# Attempt to connect to the website with retries
max_retries = 3
retry_count = 0
connected = False

while not connected and retry_count < max_retries:
    try:
        renew_tor_ip()  # Renew TOR IP address before loading the website
        driver.get(url)

        # Get the title of the website using Selenium
        title = driver.title.strip()
        print("Website Title:", title)
        connected = True

    except Exception as e:
        print("Error:", str(e))
        retry_count += 1
        if retry_count < max_retries:
            print(f"Retrying in 5 seconds (Retry {retry_count}/{max_retries})")
            time.sleep(5)
        else:
            print("Max retry count reached. Exiting.")

driver.quit()
