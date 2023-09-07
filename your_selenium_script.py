from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Configure Firefox options
options = Options()
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
options.add_argument('--log-level=DEBUG')  # Add this line to enable WebDriver logging
options.add_argument('--headless')

# Configure custom proxy settings for Firefox
proxy = webdriver.Proxy()
proxy.proxy_type = 'manual'
proxy.http_proxy = "127.0.0.1:9050"
proxy.ssl_proxy = "127.0.0.1:9050"

capabilities = webdriver.DesiredCapabilities.FIREFOX
proxy.add_to_capabilities(capabilities)

# Create the Firefox WebDriver with custom options
driver = webdriver.Firefox(options=options, desired_capabilities=capabilities)

site = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'
driver.get(site)

driver.quit()
print('Armlet Armlet')
