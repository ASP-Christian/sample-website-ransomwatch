from selenium import webdriver

# Tor SOCKS proxy configuration
tor_proxy = "socks5://127.0.0.1:9150"
proxy_options = {
    'proxy': {
        'socksProxy': tor_proxy,
        'socksVersion': 5,
    }
}

# Configure Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')  # Run Firefox in headless mode
firefox_options.add_argument('--no-sandbox')  # Required for running in a container

# Configure the WebDriver with proxy and options
driver = webdriver.Firefox(options=firefox_options, proxy=proxy_options)

# Navigate to the website
site = 'http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/'
driver.get(site)

# Perform additional actions here
print("Success, Success, Success")

# Close the WebDriver
driver.quit()
