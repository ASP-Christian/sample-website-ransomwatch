from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

# Configure Firefox to use Tor as a proxy
tor_binary = './tor_browser/Tor Browser/firefox.exe'
tor_profile = './tor_browser/tor_profile'

binary = FirefoxBinary(tor_binary)
profile = FirefoxProfile(tor_profile)

# Rest of the script remains the same


# Set up the Firefox WebDriver with the Tor settings
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=profile)

# Navigate to the Tor hidden service URL
url = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'
driver.get(url)

# Scrape the website title
title = driver.title
print(f'Title of the website: {title}')

# Close the browser
driver.quit()
