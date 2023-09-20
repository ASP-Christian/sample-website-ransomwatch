from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import requests

# Set up the TOR proxy
tor_proxy = "127.0.0.1:9150"  # Use your Tor proxy address without the scheme

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = tor_proxy
proxy.ssl_proxy = tor_proxy

capabilities = webdriver.DesiredCapabilities.FIREFOX
proxy.add_to_capabilities(capabilities)

# Check if the Tor proxy is reachable
try:
    requests.get("http://check.torproject.org", proxies={"http": tor_proxy, "https": tor_proxy}, timeout=10)
except requests.RequestException as e:
    print("Failed to connect to the Tor proxy:", str(e))
    exit(1)

# Wait for Tor proxy to fully start (adjust sleep duration as needed)
time.sleep(5)

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
