import requests
from lxml import html

def makeRequests():
    r1 = requests.get('https://www.digitalocean.com/pricing/')
    r2 = requests.get('https://www.vultr.com/pricing/')
    r3 = requests.get('https://www.packet.net/bare-metal/')
    print(r1.text)

makeRequests()
