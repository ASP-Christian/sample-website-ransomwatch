from selenium import webdriver

# Set the paths to Geckodriver and Firefox executable
geckodriver_path = '/path/to/geckodriver-directory/geckodriver'
firefox_binary_path = '/path/to/firefox-executable/firefox'

# Set Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = firefox_binary_path

# Initialize the Firefox WebDriver with explicit paths
driver = webdriver.Firefox(executable_path=geckodriver_path, options=firefox_options)

# Navigate to the website
url = "https://example.com"  # Replace with the URL of the website you want to scrape
driver.get(url)

# Get the title of the website
title = driver.title

# Print the title
print("Title of the website:", title)

# Close the browser
driver.quit()
