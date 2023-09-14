from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set up Firefox options for headless mode
options = Options()
options.headless = True

# Initialize the Firefox WebDriver with the specified options
driver = webdriver.Firefox(options=options)

# Replace 'https://example.com' with the URL of the website you want to extract the title from
url = 'https://www.apps.disneyplus.com/ph/shows/family-guy/1260024995/better-off-meg/1260025867/watch?episodeNumber=17&filters=content_type%3Depisode&seasonId=71'
driver.get(url)

# Extract and print the title of the webpage
title = driver.title
print(f'Title of the webpage: {title}')

# Close the browser
driver.quit()
