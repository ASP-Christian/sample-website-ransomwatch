import random
import string
import json
import requests
import socks
import socket  # Add this line
from requests.exceptions import ConnectionError

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
        # Configure requests to use Tor
        session = requests.Session()
        session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

        # Use SOCKS proxy for requests
        socks.set_default_proxy(socks.SOCKS5, 'localhost', 9050)
        socket.socket = socks.socksocket

        response = session.get(link, timeout=5)

        if response.status_code == 200:
            return "Active"
    except ConnectionError:
        pass
    return "Not Active"

# Load base codes from a JSON file
with open('Overall_data/small_sample.json') as json_file:
    data = json.load(json_file)
    base_codes = [group['group'] for group in data]

# Number of codes to generate
num_codes = 1000

# Generate and store the codes
generated_codes = []
for _ in range(num_codes):
    random_base_code = random.choice(base_codes)
    generated_code = generate_code(random_base_code)
    generated_codes.append(generated_code)

# Check if the generated codes are active using Tor
for code in generated_codes:
    status = check_active(code)
    print(f"{code}: {status}")
