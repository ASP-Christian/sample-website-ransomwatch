from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import requests

# Set up the TOR proxy
tor_proxy = "127.0.0.1:9150"  # Use your Tor proxy address without the scheme

# Function to check if Tor proxy is reachable
def is_tor_proxy_reachable():
    try:
        requests.get("http://check.torproject.org", proxies={"http": tor_proxy, "https": tor_proxy}, timeout=10)
        return True
    except requests.RequestException as e:
        print("Failed to connect to the Tor proxy:", str(e))
        return False

# Wait for Tor proxy to fully start (adjust sleep duration as needed)
max_attempts = 30
delay = 5
for _ in range(max_attempts):
    if is_tor_proxy_reachable():
        print("Tor proxy is reachable.")
        break
    time.sleep(delay)
else:
    print("Failed to reach Tor proxy after waiting.")
    exit(1)

# Set up headless mode for Firefox
options = webdriver.FirefoxOptions()
options.headless = True

# Create a Firefox WebDriver instance with the options
driver = webdriver.Firefox(options=options)

# Navigate to the website
site = 'http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/'
driver.get(site)
print("Success!")

# You can perform additional actions here

# Close the driver when done
driver.quit()
