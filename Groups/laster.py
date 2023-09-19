from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# TOR proxy settings for Firefox
tor_proxy = {
    'proxyType': "manual",
    'socksProxy': "localhost:9050",  # Tor SOCKS5 proxy
    'socksVersion': 5,
}

# URL of the onion website
url = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'

# Configure Firefox to use TOR proxy settings in headless mode
firefox_options = Options()
firefox_options.add_argument('-headless')
firefox_options.add_argument('--proxy-server=socks5://localhost:9050')

# Start Firefox with TOR settings
driver = webdriver.Firefox(options=firefox_options)

try:
    driver.get(url)

    # Get the title of the website using Selenium
    title = driver.title.strip()
    print("Website Title:", title)

except Exception as e:
    print("Error:", str(e))

finally:
    driver.quit()
print("DONE")