from selenium import webdriver
from selenium.common.exceptions import WebDriverException


tor_proxy = "socks5://127.0.0.1:9150"
options = webdriver.FirefoxOptions()
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '127.0.0.1')
options.set_preference('network.proxy.socks_port', 9150)
options.set_preference('network.proxy.socks_remote_dns', True)

options.add_argument('-headless')

driver = webdriver.Firefox(options=options)

site = 'https://chrisodrogla.github.io/My-Website-Portfolio/'
print("Accessing URL:", site)  # Print the URL you are trying to access
driver.get(site)


driver.quit()
