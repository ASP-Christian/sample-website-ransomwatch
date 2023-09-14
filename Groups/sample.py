from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set up Firefox options for headless mode
options = Options()
options.headless = True

# Set up the Tor SOCKS proxy
tor_proxy_port = 9150  # Replace with the actual SOCKS proxy port if it's different

# Define the Firefox profile with the proxy settings
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("network.proxy.type", 1)
firefox_profile.set_preference("network.proxy.socks", "127.0.0.1")
firefox_profile.set_preference("network.proxy.socks_port", tor_proxy_port)

# Pass the profile to the Firefox WebDriver options
options.profile = firefox_profile

# Initialize the Firefox WebDriver with the specified options
driver = webdriver.Firefox(options=options)

# Replace 'https://example.com' with the URL of the website you want to visit
url = 'https://example.com'
driver.get(url)

# Extract and print the title of the webpage
title = driver.title
print(f'Title of the webpage: {title}')

# Close the browser
driver.quit()
