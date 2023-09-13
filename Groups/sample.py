from selenium import webdriver
from selenium.common.exceptions import WebDriverException

try:
    tor_proxy = "socks5://127.0.0.1:9150"
    options = webdriver.FirefoxOptions()
    options.set_preference('network.proxy.type', 1)
    options.set_preference('network.proxy.socks', '127.0.0.1')
    options.set_preference('network.proxy.socks_port', 9150)
    options.set_preference('network.proxy.socks_remote_dns', True)

    options.add_argument('-headless')

    driver = webdriver.Firefox(options=options)

    site = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'
    print("Accessing URL:", site)  # Print the URL you are trying to access
    driver.get(site)

    # Get and print the title of the website
    print("Title:", driver.title)

except WebDriverException as e:
    print("WebDriverException:", str(e))
except Exception as e:
    print("An unexpected error occurred:", str(e))

finally:
    # Close the driver
    driver.quit()
