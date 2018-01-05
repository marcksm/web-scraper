import requests
from lxml import html
from computer import Computer

def makeRequests():
    r1 = requests.get('https://www.digitalocean.com/pricing/')
#    r2 = requests.get('https://www.vultr.com/pricing/')
#    r3 = requests.get('https://www.packet.net/bare-metal/')
    tree = html.fromstring(r1.text)
    computers = tree.xpath('//div[@class="PriceBlock-container"]')
    return computers

def buildComputer(comp_tree):

    price_mo = comp_tree.xpath('div/div/div/span[@class="PriceBlock-num"]')[0].text_content()
    price_hr = comp_tree.xpath('div/div/div[@class="u-flex u-flexCenter PriceBlock--secondary"]')[0].text_content()
    mem_ram = comp_tree.xpath('div/ul/li/span')[0].text_content()
    cpus = comp_tree.xpath('div/ul/li')[1].text_content()
    mem_ssd = comp_tree.xpath('div/ul/li')[2].text_content()
    bandwidth = comp_tree.xpath('div/ul/li')[3].text_content()
    computer = Computer('service', 'name', price_hr, price_mo, cpus, mem_ram, mem_ssd, bandwidth)
    return computer

def computers():
    comp = makeRequests()
    #print(len(comp))
    for i in range (0, len(comp)):
        computer = buildComputer(comp[i])
        computer.showData()
        #sqldata=computer.getData()
        #save to sqllite
        print('\n')

computers()
