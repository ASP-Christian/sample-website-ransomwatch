from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from stem import Signal
from stem.control import Controller

# Function to renew TOR identity
def renew_tor_identity():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

# Set up Firefox options for headless mode
options = Options()
options.headless = True

# Configure the Firefox WebDriver to use TOR as a proxy
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)  # Default TOR SOCKS port

# Initialize the Firefox WebDriver with the specified options and TOR proxy
driver = webdriver.Firefox(firefox_profile=profile, options=options)

# Replace 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/' with your .onion website URL
url = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'
driver.get(url)

# Extract and print the title of the webpage
title = driver.title
print(f'Title of the webpage: {title}')

# Renew TOR identity to change the exit node (optional)
renew_tor_identity()

# Close the browser
driver.quit()
