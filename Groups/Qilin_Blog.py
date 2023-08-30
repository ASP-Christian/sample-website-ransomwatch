from selenium import webdriver
import pandas as pd
import time

# set up TOR and the TOR browser
tor_proxy = "socks5://127.0.0.1:9150"
options = webdriver.FirefoxOptions()
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '127.0.0.1')
options.set_preference('network.proxy.socks_port', 9150)
options.set_preference('network.proxy.socks_remote_dns', True)

# Set the WebDriver to run in headless mode
options.headless = True

# Create a Firefox WebDriver instance with the options
driver = webdriver.Firefox(options=options)

# navigate to the website
site = 'http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/'
driver.get(site)
print("Success!, Success!, Success! , Success!, Success!, Success!, Success!, Success!, Success!, Success!, Success!, Success!")

# You can perform additional actions here

# Close the driver when done
driver.quit()
