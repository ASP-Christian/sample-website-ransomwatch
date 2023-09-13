from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from stem import Signal
from stem.control import Controller

# Set up Firefox options for headless mode
options = Options()
options.headless = True

# Initialize the Firefox WebDriver with the specified options
driver = webdriver.Firefox(options=options)

# Change Tor identity (get a new IP address)
def change_identity():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_password_here")  # Replace with your Tor control password
        controller.signal(Signal.NEWNYM)

# Change Tor identity to get a new IP address
change_identity()

# Replace 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/' with the actual .onion URL
url = 'https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'
driver.get(url)

# Extract and print the title of the webpage
title = driver.title
print(f'Title of the webpage: {title}')

# Close the browser
driver.quit()
