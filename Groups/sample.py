from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import stem.process
import time

# Set up TOR proxy
tor_process = stem.process.launch_tor_with_config(
    config={
        'SocksPort': '9051',  # Use a different SocksPort
        'ControlPort': '9052',  # Use a different ControlPort
    },
)

# Set up Firefox with the TOR proxy
firefox_options = Options()
firefox_options.add_argument('--proxy-server=socks5://localhost:9051')  # Use the new SocksPort
firefox_options.add_argument('--headless')  # Run in headless mode (optional)
firefox_options.add_argument('--ignore-certificate-errors')  # Ignore certificate errors (optional)

# Configure Firefox to use TOR for DNS resolution
firefox_options.add_argument('--dns-over-https=https://1.1.1.1/dns-query')  # Use Cloudflare DNS over HTTPS

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(options=firefox_options)

# Navigate to the Onion site
onion_site_url = "https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/"
driver.get(onion_site_url)

# Wait for the page to load (you can adjust the wait time as needed)
time.sleep(5)

# Get the title of the page
title = driver.title
print("Title of the Onion site:", title)

# Close the WebDriver and TOR proxy
driver.quit()
tor_process.terminate()
