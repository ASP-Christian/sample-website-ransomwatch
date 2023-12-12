from bs4 import BeautifulSoup
import requests
import random
from stem import Signal
from stem.control import Controller

Search_Bar = "vice"
yourquery = Search_Bar
if " " in yourquery:
    yourquery = yourquery.replace(" ", "+")

url = "https://ahmia.fi/search/?q={}".format(yourquery)

# Set up some fake user agents
ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
    "Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
    "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
]
ua = random.choice(ua_list)
headers = {'User-Agent': ua}

website = url
response = requests.get(website)
soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find_all('li', {'class': 'result'})


# Function to renew the TOR IP address
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="YOUR_TOR_PASSWORD")
        controller.signal(Signal.NEWNYM)


for result in results:
    try:
        onion_link = result.cite.get_text()
        # Add "http://" if not present
        if not onion_link.startswith("http://"):
            onion_link = "http://" + onion_link
    except:
        onion_link = 'n/a'

    try:
        title = result.a.text.strip()
    except:
        title = 'n/a'

    try:
        description = result.p.text
    except:
        description = 'n/a'

    try:
        # Renew TOR IP before making a request
        renew_tor_ip()

        # Make a request using TOR proxy
        response = requests.get(onion_link, headers=headers,
                                proxies={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})

        status_code = response.status_code
        print(f"Onion Link: {onion_link}\nTitle: {title}\nDescription: {description}\nStatus Code: {status_code}\n")
    except Exception as e:
        print(f"Error for Onion Link: {onion_link}\nError Message: {str(e)}\n")
