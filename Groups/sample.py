from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# Set up Firefox options
firefox_options = Options()
firefox_options.headless = True  # Run in headless mode (optional)

# Configure Firefox to use TOR proxy for DNS resolution
firefox_options.set_preference("network.proxy.type", 1)
firefox_options.set_preference("network.proxy.socks", "127.0.0.1")
firefox_options.set_preference("network.proxy.socks_port", 9050)  # Use TOR SocksPort

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(options=firefox_options)

# Navigate to the Onion site
onion_site_url = "https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/"
driver.get(onion_site_url)

# Wait for the page to load (you can adjust the wait time as needed)
time.sleep(5)

# Get the title of the page
title = driver.title
print("Title of the Onion site:", title)

# Close the WebDriver
driver.quit()
