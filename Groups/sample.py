from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from stem import Signal
from stem.control import Controller

# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument('--headless')  # Run in headless mode (optional)

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(options=firefox_options)

# Configure TOR control port
with Controller.from_port(port=9052) as controller:
    controller.authenticate()  # Authenticate with the TOR control port

    # Get a new TOR identity (change IP)
    controller.signal(Signal.NEWNYM)

# Configure Firefox to use TOR's SOCKS proxy
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)  # Use TOR's SocksPort

# Set the Firefox profile
driver = webdriver.Firefox(firefox_profile=profile, options=firefox_options)

# Navigate to the Onion site
onion_site_url = "https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/"
driver.get(onion_site_url)

# Wait for the page to load (you can adjust the wait time as needed)
time.sleep(5)

# Get the title of the page
title = driver.title
print("Title of the Onion site:", title)

# Close the WebDriver
driver.quit()
