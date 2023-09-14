from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set up Firefox options for headless mode
options = Options()
options.headless = True

# Create a Firefox profile with the proxy settings
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("network.proxy.type", 1)  # Use manual proxy configuration
firefox_profile.set_preference("network.proxy.socks", "127.0.0.1")  # Replace with the proxy IP address
firefox_profile.set_preference("network.proxy.socks_port", 9150)  # Replace with the Tor SOCKS proxy port

# Initialize the Firefox WebDriver with the specified options and profile
driver = webdriver.Firefox(firefox_profile=firefox_profile, options=options)

# Replace 'https://example.com' with the URL of the website you want to visit
url = 'https://chrisodrogla.github.io/My-Website-Portfolio/'

driver.get(url)

# Extract and print the title of the webpage
title = driver.title
print(f'Title of the webpage: {title}')

# Close the browser
driver.quit()


