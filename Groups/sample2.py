from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

# Set up the TOR proxy
tor_proxy = "127.0.0.1:9150"  # Use your Tor proxy address without the scheme

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = tor_proxy
proxy.ssl_proxy = tor_proxy

capabilities = webdriver.DesiredCapabilities.FIREFOX
proxy.add_to_capabilities(capabilities)

# Set up headless mode for Firefox
options = webdriver.FirefoxOptions()
options.headless = True

# Create a Firefox WebDriver instance with the options
driver = webdriver.Firefox(capabilities=capabilities, options=options)

# Navigate to the website
site = 'http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/'
driver.get(site)
print("Success!")

# You can perform additional actions here

# Close the driver when done
driver.quit()
