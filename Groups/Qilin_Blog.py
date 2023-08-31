from selenium import webdriver

# Set up TOR and the TOR browser
tor_proxy = "socks5://127.0.0.1:9150"
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '127.0.0.1')
options.set_preference('network.proxy.socks_port', 9150)
options.set_preference('network.proxy.socks_remote_dns', True)

# Set the WebDriver executable path
driver_path = './geckodriver'  # Update the path here
driver = webdriver.Firefox(executable_path=driver_path, options=options)

# Navigate to the website
site = 'http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/'
driver.get(site)

# Perform additional actions here
print("Success, Success, Success")
# Close the driver when done
driver.quit()
