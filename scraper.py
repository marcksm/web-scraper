import requests
from lxml import html
import re

def makeRequests():
    r1 = requests.get('https://www.digitalocean.com/pricing/')
    r2 = requests.get('https://www.vultr.com/pricing/')
    r3 = requests.get('https://www.packet.net/bare-metal/')
    tree = html.fromstring(r1.text)
    computers = tree.xpath('//div[@class="PriceBlock-container"]')
    #print (computers[0].text_content())
    return computers

def computers():
    comp = makeRequests()
    pc = comp[0]
    price_mo = pc.xpath('div/div/div/span[@class="PriceBlock-num"]/text()')
    price_hr = re.findall("\d+\.\d+", pc.xpath('div/div/div[@class="u-flex u-flexCenter PriceBlock--secondary"]/text()')[0])
    mem_ram = pc.xpath('div/ul/li')[0]
    cpus = pc.xpath('div/ul/li')[1]
    mem_sdd = pc.xpath('div/ul/li')[2]
    bandwidth = pc.xpath('div/ul/li')[3]
    print (price_mo)
    print (price_hr)
    print (cpus.text_content())
computers()
