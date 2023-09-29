import requests
import socks
import socket
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

# Configure Tor proxy settings
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket


# Function to renew Tor circuit
def renew_tor_circuit():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="YOUR_TOR_PASSWORD")
        controller.signal(Signal.NEWNYM)


# URL of the website you want to scrape
url = "http://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion"

# Renew the Tor circuit before making a request
renew_tor_circuit()

try:
    # Send a GET request through Tor
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and print the title
        title = soup.title.string
        print(f"Title: {title}")

    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
