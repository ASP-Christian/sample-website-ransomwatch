from selenium import webdriver

# Configure your HTTP proxy here
proxy_host = "your_proxy_host"  # Replace with your proxy host (e.g., "proxy.example.com")
proxy_port = 8080  # Replace with your proxy port

# Set up the proxy in Selenium
proxy = f"{proxy_host}:{proxy_port}"

options = webdriver.FirefoxOptions()
options.add_argument(f"--proxy-server={proxy}")

# You can also add other Firefox options as needed
# options.add_argument("-headless")

driver = webdriver.Firefox(options=options)

site = 'https://chrisodrogla.github.io/My-Website-Portfolio/'
print("Accessing URL:", site)  # Print the URL you are trying to access
driver.get(site)

# Get and print the title of the website
print("Title:", driver.title)

# Don't forget to close the driver when done
driver.quit()
