from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# URL to scrape
url = "https://chrisodrogla.github.io/My-Website-Portfolio/"

# Set up Firefox options
firefox_options = Options()
firefox_options.headless = True  # Run Firefox in headless mode to avoid GUI

# Initialize the Firefox WebDriver with options
driver = webdriver.Firefox(options=firefox_options)

try:
    # Open the URL in the WebDriver
    driver.get(url)

    # Get the title of the webpage
    title = driver.title

    # Print the title
    print("Website Title:", title)

finally:
    # Close the WebDriver
    driver.quit()
