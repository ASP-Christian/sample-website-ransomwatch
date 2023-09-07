from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

tor_proxy = "socks5://127.0.0.1:9050"
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9050)
profile.set_preference("network.proxy.socks_version", 5)

driver = webdriver.Firefox(firefox_profile=profile)
