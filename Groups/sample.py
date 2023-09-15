# import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Set up Firefox options
firefox_options = Options()
firefox_options.headless = True  # Run Firefox in headless mode (no GUI)

# Create a Firefox WebDriver instance
driver = webdriver.Firefox(
    executable_path="./geckodriver",  # Path to geckodriver executable
    options=firefox_options
)

# Visit a website (e.g., example.com)
driver.get("https://example.com")

# Perform scraping actions here
# For example, let's get the page title
page_title = driver.title
print("Page Title:", page_title)

# Cleanup and close the browser
driver.quit()
