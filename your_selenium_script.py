from selenium import webdriver

tor_proxy = "socks5://127.0.0.1:9150"  # Tor proxy address

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9150)

driver = webdriver.Firefox(firefox_profile=profile)
driver.get('https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/')
# Your scraping code here
print('Armlet Gibaho')
driver.quit()
