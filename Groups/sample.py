from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

# Set up Firefox options for headless mode
options = Options()
options.headless = True

# Set up the Tor SOCKS proxy
tor_proxy_port = 9150  # Replace with the actual SOCKS proxy port if it's different
proxy_capabilities = {
    "proxy": {
        "proxyType": "manual",
        "socksProxy": f"127.0.0.1:{tor_proxy_port}",
    }
}

# Create a DesiredCapabilities object and set the proxy
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities.update(proxy_capabilities)

# Initialize the Firefox WebDriver with the specified options and capabilities
driver = webdriver.Firefox(desired_capabilities=capabilities, options=options)

# Replace 'https://example.com' with the URL of the website you want to visit
url = 'https://example.com'
driver.get(url)

# Extract and print the title of the webpage
title = driver.title
print(f'Title of the webpage: {title}')

# Close the browser
driver.quit()
