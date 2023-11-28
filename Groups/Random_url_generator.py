import random
import string
import requests
from stem import Signal
from stem.control import Controller
from requests.exceptions import RequestException
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

# Your generated codes
generated_codes = [
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

def check_active(link):
    try:
        renew_tor_ip()
        response = requests.get(link, proxies=tor_proxy, verify=False, timeout=5)

        status_code = response.status_code

        if 200 <= status_code < 300:
            return True  # Link is active
    except RequestException as e:
        print(f"Error for {link}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {link}: {str(e)}")
    return False  # Link is not active

# Check if the generated codes are active using Tor
for code in generated_codes:
    is_active = check_active(code)
    status = "Success" if is_active else "Not Active"
    print(f"{code}: {status}")
