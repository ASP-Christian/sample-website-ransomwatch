from selenium import webdriver

# Tor SOCKS proxy configuration
tor_proxy = "socks5://127.0.0.1:9150"

# Configure Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')  # Run Firefox in headless mode
firefox_options.add_argument('--no-sandbox')  # Required for running in a container

# Set up proxy preferences
firefox_options.set_preference('network.proxy.type', 1)
firefox_options.set_preference('network.proxy.socks', '127.0.0.1')
firefox_options.set_preference('network.proxy.socks_port', 9150)
firefox_options.set_preference('network.proxy.socks_remote_dns', True)

# Configure the WebDriver with options
driver = webdriver.Firefox(options=firefox_options)

# Navigate to the website
site = 'http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/'
driver.get(site)

# Perform additional actions here
print("Success, Success, Success")

# Close the WebDriver
driver.quit()
