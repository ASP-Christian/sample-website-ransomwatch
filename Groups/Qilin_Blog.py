from selenium import webdriver

# Set up TOR and the TOR browser
tor_proxy = "socks5://127.0.0.1:9150"
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '127.0.0.1')
options.set_preference('network.proxy.socks_port', 9150)
options.set_preference('network.proxy.socks_remote_dns', True)

# Set the PATH environment variable to include the directory where geckodriver is located
import os
os.environ['PATH'] = f'{os.getcwd()}{os.pathsep}{os.environ["PATH"]}'

# Create a Firefox WebDriver instance
driver = webdriver.Firefox(options=options)

# Navigate to the website
site = 'http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/'
driver.get(site)

# Perform additional actions here
print("Success, Success, Success")
