from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
options.add_argument('--log-level=DEBUG')  # Add this line to enable WebDriver logging

driver = webdriver.Firefox(options=options)
