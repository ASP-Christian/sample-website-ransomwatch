import random
import string
import json
import requests
import socks
import socket
from requests.exceptions import ConnectionError
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
from datetime import datetime

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

def generate_code(base_code):
    # Extract the desired part from the base code
    extracted_part = base_code.split('//')[-1].split('.')[0]

    # Generate a random code based on the extracted part
    result = ""
    for char in extracted_part:
        if char.isalpha():
            result += random.choice(string.ascii_letters)
        elif char.isdigit():
            result += random.choice(string.digits)
        else:
            result += char

    # Add "http://" at the beginning and ".onion" at the end
    generated_code = "http://" + result + ".onion"
    return generated_code

def check_active(link):
    try:
        renew_tor_ip()
        response = requests.get(link, proxies=tor_proxy, verify=False, timeout=5)

        status_code = response.status_code

        if 200 <= status_code < 300:
            return True  # Link is active
    except requests.exceptions.RequestException as e:
        print(f"Error for {link}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {link}: {str(e)}")
    return False  # Link is not active

# Load base codes from a JSON file
with open('Overall_data/small_sample.json') as json_file:
    data = json.load(json_file)
    base_codes = [group['group'] for group in data]

# Number of codes to generate
num_codes = 5

# Generate and store the codes
generated_codes = []
for _ in range(num_codes):
    random_base_code = random.choice(base_codes)
    generated_code = generate_code(random_base_code)
    generated_codes.append(generated_code)

# Check if the generated codes are active using Tor
for code in generated_codes:
    is_active = check_active(code)
    status = "Success" if is_active else "Not Active"
    print(f"{code}: {status}")
