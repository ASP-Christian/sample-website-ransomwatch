from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Configure Firefox options
options = Options()
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
options.add_argument('--log-level=DEBUG')  # Add this line to enable WebDriver logging
options.add_argument('--headless')

# Configure custom DNS settings
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('network.proxy.socks', '127.0.0.1')
firefox_profile.set_preference('network.proxy.socks_port', 9050)
firefox_profile.set_preference('network.proxy.socks_remote_dns', True)  # Use Tor for DNS resolution

# Create the Firefox WebDriver with custom options and profile
driver = webdriver.Firefox(firefox_profile=firefox_profile, options=options)

site = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'
driver.get(site)

driver.quit()
print('Armlet Armlet')
