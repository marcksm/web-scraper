import requests
from lxml import html
from computer import Computer
import sqlitedatabase

def makeRequests():
    global r1, r2, r3
    r1 = requests.get('https://www.digitalocean.com/pricing/')
    r2 = requests.get('https://www.vultr.com/pricing/')
    #r3 = requests.get('https://www.packet.net/bare-metal/')
    tree1 = html.fromstring(r1.text)
    tree2 = html.fromstring(r2.text)
    #tree3 = html.fromstring(r3.text)
    location1 = tree1.xpath('//div[@class="PriceBlock-container"]')
    location2 = tree2.xpath('//div[@class="packages-row row"]/div[@class="col-sm-3 col-xs-6"]')
    #location3 = tree3.xpath('//div[@class="PriceBlock-container"]')
    locations = [location1, location2]
    return locations

def extractR1(comp_tree):
    price_mo = comp_tree.xpath('div/div/div/span[@class="PriceBlock-num"]')[0].text_content()
    price_hr = comp_tree.xpath('div/div/div[@class="u-flex u-flexCenter PriceBlock--secondary"]')[0].text_content()
    mem_ram = comp_tree.xpath('div/ul/li/span')[0].text_content()
    cpus = comp_tree.xpath('div/ul/li')[1].text_content()
    mem_ssd = comp_tree.xpath('div/ul/li')[2].text_content()
    bandwidth = comp_tree.xpath('div/ul/li')[3].text_content()
    computer = Computer(r1.url, 'name', price_hr, price_mo, cpus, mem_ram, mem_ssd, bandwidth)
    return computer

def extractR2(comp_tree):
    price_mo = comp_tree.xpath('a/div/span[@class="package-price"]/@data-monthly')[0]
    price_hr = comp_tree.xpath('a/div/span[@class="package-price"]/@data-hourly')[0]
    print(price_mo)
    mem_ram = comp_tree.xpath('a/div[@class="package-body"]/ul/li')[1].text_content()
    cpus = comp_tree.xpath('a/div[@class="package-body"]/ul/li')[0].text_content()
    mem_ssd = comp_tree.xpath('a/div/h3')[0].text_content()
    bandwidth = comp_tree.xpath('a/div[@class="package-body"]/ul/li')[2].text_content()
    computer = Computer(r2.url, 'name', price_hr, price_mo, cpus, mem_ram, mem_ssd, bandwidth)
    computer.showData()
    return computer

def extractR3(comp_tree):
    price_mo = comp_tree.xpath('div/div/div/span[@class="PriceBlock-num"]')[0].text_content()
    price_hr = comp_tree.xpath('div/div/div[@class="u-flex u-flexCenter PriceBlock--secondary"]')[0].text_content()
    mem_ram = comp_tree.xpath('div/ul/li/span')[0].text_content()
    cpus = comp_tree.xpath('div/ul/li')[1].text_content()
    mem_ssd = comp_tree.xpath('div/ul/li')[2].text_content()
    bandwidth = comp_tree.xpath('div/ul/li')[3].text_content()
    computer = Computer(r1.url, 'name', price_hr, price_mo, cpus, mem_ram, mem_ssd, bandwidth)
    return computer

def extractData():
    sqlitedatabase.makeConnection()
    sqlitedatabase.createTable()
    locations = makeRequests()
    for k in range (0, len(locations)):
        comp = locations[k]
        for i in range (0, len(comp)):
            if k == 0:
                computer = extractR1(comp[i])
            elif k == 1:
                computer = extractR2(comp[i])
            else
                computer = extractR3(comp[i])
            sqlitedatabase.tableInsert(computer.toSQL())
    sqlitedatabase.tableSave()
    sqlitedatabase.closeConnection()

extractData()
