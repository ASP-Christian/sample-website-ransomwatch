from selenium import webdriver

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