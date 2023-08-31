from selenium import webdriver
import pandas as pd
import time
import os

tor_proxy = os.getenv('TOR_PROXY', "socks5://127.0.0.1:9150")

options = webdriver.FirefoxOptions()
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '127.0.0.1')
options.set_preference('network.proxy.socks_port', 9150)
options.set_preference('network.proxy.socks_remote_dns', True)
options.headless = True

driver = webdriver.Firefox(options=options)

site = 'http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/'
driver.get(site)
print("Success! The script ran successfully!")

# Additional actions you want to perform here

driver.quit()
