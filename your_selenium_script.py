from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# Configure Firefox options
options = Options()
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
options.add_argument('--log-level=DEBUG')  # Add this line to enable WebDriver logging
options.add_argument('--headless')

# Create the Firefox WebDriver with custom options
driver = webdriver.Firefox(options=options)

site = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'

# Add a delay before accessing the site (adjust the time as needed)
time.sleep(40)  # Wait for 10 seconds

driver.get(site)

driver.quit()
print('Armlet Armlet')
