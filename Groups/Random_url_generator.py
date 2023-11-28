import random
import string
import json
import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

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

        if status_code == 200:
            return True, status_code  # Link is active

    except requests.exceptions.RequestException as e:
        print(f"Error for {link}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {link}: {str(e)}")
    
    return False, status_code  # Link is not active

# Add the URLs for testing
test_urls = [
    "https://ahmia.fi/",
    "http://nq4zyac4ukl4tykmidbzgdlvaboqeqsemkp4t35bzvjeve6zm2lqcjid.onion",
    "https://3f7nxkjway3d223j27lyad7v5cgmyaifesycvmwq7i7cbs23lb6llryd.onion",
    "http://4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion",
    "http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion",
    "http://jbeg2dct2zhku6c2vwnpxtm2psnjo2xnqvvpoiiwr5hxnc6wrp3uhnad.onion",
    "http://bianlianlbc5an4kgnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad.onion",
    "http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/",
    "http://sbc2zv2qnz5vubwtx3aobfpkeao6l4igjegm3xx7tk5suqhjkp5jxtqd.onion/",
    "http://7ukmkdtyxdkdivtjad57klqnd3kdsmq6tp45rrsxqnu76zzv3jvitlqd.onion/",
    "http://5n4qdkw2wavc55peppyrelmb2rgsx7ohcb2tkxhub2gyfurxulfyd3id.onion/"
]

# Check status for each test URL
for url in test_urls:
    is_active, status_code = check_active(url)
    status = "Success" if is_active else "Not Active"
    print(f"{url}: {status}, Status Code: {status_code}")
