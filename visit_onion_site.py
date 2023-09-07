import os
from selenium import webdriver
from stem import Signal
from stem.control import Controller

# Set the TOR_BROWSER_PATH environment variable to the path where you extracted the TOR browser
tor_browser_path = os.environ.get('TOR_BROWSER_PATH')

# Start TOR browser with Selenium
tor_browser = os.path.join(tor_browser_path, 'Browser', 'firefox')
driver = webdriver.Firefox(executable_path=os.path.join(tor_browser, 'geckodriver'))

# Create a new TOR control connection
with Controller.from_port(port=9051) as controller:
    controller.authenticate()  # Authenticate with the TOR control port

    # Request a new TOR identity (change IP)
    controller.signal(Signal.NEWNYM)

    # Visit the Onion site
    driver.get("https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/")

# Close the TOR browser
driver.quit()
print('successssssssssssssssssssssssssssssssssssssssssssss')