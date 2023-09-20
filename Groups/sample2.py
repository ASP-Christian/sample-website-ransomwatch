from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
tor_proxy = "socks5://127.0.0.1:9150"

# Set up the TOR proxy
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = f"{tor_proxy}"  # Use your tor_proxy variable here
proxy.socks_proxy = f"{tor_proxy}"  # Use your tor_proxy variable here
proxy.ssl_proxy = f"{tor_proxy}"  # Use your tor_proxy variable here

capabilities = webdriver.DesiredCapabilities.FIREFOX
proxy.add_to_capabilities(capabilities)

# Create a Firefox WebDriver instance with the options
driver = webdriver.Firefox(capabilities=capabilities)

# Navigate to the website
site = 'http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/'
driver.get(site)
print("Success!")

# You can perform additional actions here

# Close the driver when done
driver.quit()
