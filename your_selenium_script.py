from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')

driver = webdriver.Firefox(options=options)

