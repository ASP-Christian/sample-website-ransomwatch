from selenium import webdriver

# Set up the WebDriver (you may need to adjust the path to geckodriver)
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

# Navigate to the website
driver.get("https://chrisodrogla.github.io/My-Website-Portfolio/")

# Get the title of the website
title = driver.title

# Print the title to the console (you can modify this part as needed)
print("Website Title:", title)

# Close the WebDriver
driver.quit()
