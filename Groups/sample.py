from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from stem import Signal
from stem.control import Controller
import time

# Function to change Tor IP address
def change_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_password")  # Replace with your Tor password
        controller.signal(Signal.NEWNYM)

# Set up Firefox with Tor proxy
binary = FirefoxBinary()  # No need to specify the binary path
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9050)


# Create a Firefox WebDriver instance
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=profile)

# Navigate to the website
url = "https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/"
driver.get(url)

# Wait for the page to load (adjust the sleep time as needed)
time.sleep(10)

# Scrape the title
title = driver.title
print("Title:", title)

# Close the Firefox WebDriver
driver.quit()

# Change Tor IP address to avoid IP blocking
change_tor_ip()
