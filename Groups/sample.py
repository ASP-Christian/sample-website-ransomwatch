from selenium import webdriver

# Set up the Firefox WebDriver with geckodriver (no need to specify path)
driver = webdriver.Firefox()

# Navigate to the website
url = "https://chrisodrogla.github.io/My-Website-Portfolio/"
driver.get(url)

# Get the title of the website
title = driver.title

# Print the title to the console
print("Website Title:", title)

# Close the WebDriver
driver.quit()
