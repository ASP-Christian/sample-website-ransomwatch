import os
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup


# Function to renew the TOR IP address
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="YOUR_TOR_PASSWORD")
        controller.signal(Signal.NEWNYM)


# TOR proxy settings
tor_proxy = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050',
}

# URL of the onion website
url = 'https://3f7n123123123123xkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion/'

# Send a request through the TOR proxy with certificate verification disabled
try:
    renew_tor_ip()  # Renew TOR IP address before making the request
    response = requests.get(url, proxies=tor_proxy, verify=False)

    # Get the status code
    status_code = response.status_code

    if status_code == 404:
        status_message = "Not Found"
        is_active = False
    elif status_code >= 200 and status_code < 300:
        status_message = "Success"
        is_active = True
    elif status_code >= 400 and status_code < 500:
        status_message = "Client Error"
        is_active = False
    elif status_code >= 500 and status_code < 600:
        status_message = "Server Error"
        is_active = False
    else:
        status_message = "Unknown"
        is_active = False

    print("Status Code:", status_code)
    print("Status Message:", status_message)
    print("Website Active:", is_active)

except requests.exceptions.RequestException as e:
    if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 404:
        print("Status Code: 404")
        print("Status Message: Not Found")
        print("Website Active: False")
    else:
        print("Error:", str(e))
except Exception as e:
    print("Error:", str(e))
