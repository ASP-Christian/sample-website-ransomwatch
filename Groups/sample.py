from selenium import webdriver

# Set the path to Geckodriver executable
geckodriver_path = '/path/to/geckodriver-directory/geckodriver'

# Set Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = '/path/to/firefox-executable/firefox'

# Set Geckodriver path as a system property
webdriver.Firefox(executable_path=geckodriver_path, firefox_options=firefox_options, service_log_path='geckodriver.log')

# Initialize the Firefox WebDriver
driver = webdriver.Firefox()

# Navigate to the website
url = "https://example.com"  # Replace with the URL of the website you want to scrape
driver.get(url)

# Get the title of the website
title = driver.title

# Print the title
print("Title of the website:", title)

# Close the browser
driver.quit()
