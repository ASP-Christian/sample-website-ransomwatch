from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException

options = Options()
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
options.add_argument('--log-level=DEBUG')  # Add this line to enable WebDriver logging
options.add_argument('--headless')

# Adjust the URL to the onion site you want to visit
onion_url = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'

try:
    driver = webdriver.Firefox(options=options)

    # Visit the onion site
    driver.get(onion_url)

    # Get and print the title of the site
    site_title = driver.title
    print(f'Title of the site: {site_title}')

except WebDriverException as e:
    print(f'Selenium WebDriver Error: {str(e)}')
except Exception as e:
    print(f'An error occurred: {str(e)}')
finally:
    # Close the browser when done or if an error occurs
    if 'driver' in locals():
        driver.quit()
