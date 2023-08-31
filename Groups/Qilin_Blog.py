import os
from selenium import webdriver
import pandas as pd
import time

# Read proxy details from environment variables
tor_proxy = f"socks5://{os.environ['ONION_PROXY_URL']}:{os.environ['ONION_PROXY_PORT']}"
tor_username = os.environ['ONION_PROXY_USERNAME']
tor_password = os.environ['ONION_PROXY_PASSWORD']

options = webdriver.FirefoxOptions()
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', tor_proxy)
options.set_preference('network.proxy.socks_port', int(os.environ['ONION_PROXY_PORT']))
options.set_preference('network.proxy.socks_remote_dns', True)
options.headless = True

# Set Tor proxy authentication
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.socks_username", tor_username)
profile.set_preference("network.proxy.socks_password", tor_password)

# Create a Firefox WebDriver instance with the options
driver = webdriver.Firefox(options=options, firefox_profile=profile)

# navigate to the website
site = 'http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/'
driver.get(site)
print("Success! Connected via Tor.")

# You can perform additional actions here

# Close the driver when done
driver.quit()
