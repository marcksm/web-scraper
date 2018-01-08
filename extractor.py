import requests
from lxml import html
from computer import Computer
import sqlitedatabase
import re
import string
import random

global stack
stack = []

def makeRequests():
    global r1, r2, r3, r4
    r1 = requests.get('https://www.digitalocean.com/pricing/')
    r2 = requests.get('https://www.vultr.com/pricing/')
    r3 = requests.get('https://www.packet.net/bare-metal/')
    r4 = requests.get('https://www.vultr.com/pricing/dedicatedcloud/')

def name_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def buildTrees():
    tree1 = html.fromstring(r1.text)
    tree2 = html.fromstring(r2.text)
    tree3 = html.fromstring(r3.text)
    location1 = tree1.xpath('//div[@class="PriceBlock-container"]')
    location2 = tree2.xpath('//div[@class="packages-row row"]/div[@class="col-sm-3 col-xs-6"]')
    location3 = tree3.xpath('//article[@class="pricing-item col-3"]')
    locations = [location1, location2, location3]
    return locations

def extractR1(comp_tree):
    tree=comp_tree
    print ("------------------------------------------------------------------------------------------------------------------------")
    stack.clear()
    explore(tree, 'RAM')
    build(stack)
    print (stack)
    stack.clear()
    print ("------------------------------------------------------------------------------------------------------------------------")
    name = 'PC_' + name_generator()
    price_mo = comp_tree.xpath('div/div/div/span[@class="PriceBlock-num"]')[0].text_content()
    price_hr = comp_tree.xpath('div/div/div[@class="u-flex u-flexCenter PriceBlock--secondary"]')[0].text_content()
    mem_ram = comp_tree.xpath('div/ul/li/span')[0].text_content()
    cpus = comp_tree.xpath('div/ul/li')[1].text_content()
    mem_ssd = comp_tree.xpath('div/ul/li')[2].text_content()
    bandwidth = comp_tree.xpath('div/ul/li')[3].text_content()
    computer = Computer(r1.url, name, price_hr, price_mo, cpus, mem_ram, mem_ssd, bandwidth)
    return computer

def extractR2(comp_tree):
    tree=comp_tree
    stack.clear()
    print ("------------------------------------------------------------------------------------------------------------------------")
    explore(tree, 'RAM')
    build(stack)
    print ("------------------------------------------------------------------------------------------------------------------------")
    name = 'PC_' + name_generator()
    print (stack)
    stack.clear()
    price_mo = comp_tree.xpath('a/div/span[@class="package-price"]/@data-monthly')[0]
    price_hr = comp_tree.xpath('a/div/span[@class="package-price"]/@data-hourly')[0]
    cpus = comp_tree.xpath('a/div[@class="package-body"]/ul/li')[0].text_content()
    mem_ram = comp_tree.xpath('a/div[@class="package-body"]/ul/li')[1].text_content()
    bandwidth = comp_tree.xpath('a/div[@class="package-body"]/ul/li')[2].text_content()
    mem_ssd = comp_tree.xpath('a/div/h3')[0].text_content()
    computer = Computer(r2.url, name, price_hr, price_mo, cpus, mem_ram, mem_ssd, bandwidth)
    return computer

def build(div_itens):
    for i in range(0, len(div_itens)):
        div_itens[i] = div_itens[i].replace('\n', ' ').replace('\r', '')
    div = ' '.join(div_itens)
    price_mo = re.search("[\$][\s]*[0-9]+[\.*[0-9]*]*[\s]*[/][\s]*[m][o][n]*", div)
    price_hr = re.search("[\$][\s]*[0-9]+[\.*[0-9]*]*[\s]*[/][\s]*[h][r|o][u]*", div)
    mem_ram = re.search("[0-9]+[\s]*[M|G|T][B][\s]*[a-zA-Z0-9- ]*[\s]*[M|R][e|A][m|M]", div)
    cpu = re.search("[0-9]+[\s]*[a-zA-Z]*[\s]*[v|C]*[C|o][P|r][Ue][s]*", div)
    if (price_mo):
        print (price_mo.group())
    if (price_hr):
        print (price_hr.group())
    if (mem_ram):
        print (mem_ram.group())
    if (cpu):
        print (cpu.group())
    print (div)


def explore(root, data):
    for i in range (0, len(root)):
        explore(root[i], data)
    if root.xpath('@data-hourly'):
        stack.append(root.xpath('@data-hourly')[0] + '/hr')
        stack.append(root.xpath('@data-monthly')[0] + '/mo')
    if (len(root) <= 1 and str(root) != "<!-- /.package -->"):
        div_data = root.text_content()
        div_data = re.sub('\s+',' ',div_data)
        stack.append(div_data.strip())

def extractR3(comp_tree):
    price_mo = comp_tree.xpath('div[@class="head"]/p[@class="price_rate price_monthly"]/span[@class="h6 fc-bold"]')[0].text_content()
    tree=comp_tree
    stack.clear()
    print ("------------------------------------------------------------------------------------------------------------------------")
    explore(tree, 'RAM')
    build(stack)
    print (stack)
    stack.clear()
    print ("------------------------------------------------------------------------------------------------------------------------")

    # for i in range (0, len (tree)):
    #     x=tree[i]
    #     for k in range (0, len (x)):
    #         g=x[k]
    #         for j in range (0, len (g)):
    #             print(g[j].text_content())
    #

    price_hr = comp_tree.xpath('div[@class="head"]/p')[0].text_content()
    name = comp_tree.xpath('div[@class="head"]/p[@class="label"]')[0].text_content()
    cpus = comp_tree.xpath('div[@class="body flex"]/span/p/b')[0].text_content()
    body = comp_tree.xpath('div[@class="body flex"]/span/p/b')
    hdd = None
    for i in range (0, len(body)):
        if re.search('RAM',body[i].text_content()):
            mem_ram = comp_tree.xpath('div[@class="body flex"]/span/p/b')[i].text_content()
        if re.search('SSD', body[i].text_content()):
            mem_ssd = comp_tree.xpath('div[@class="body flex"]/span/p/b')[i].text_content()
        if re.search('HDD', body[i].text_content()):
            hdd = comp_tree.xpath('div[@class="body flex"]/span/p/b')[i].text_content()
            hdd_size = float(re.findall("[0-9]+\.*[0-9]*", hdd)[0])
            hdd_type = re.findall("[a-zA-Z]+", hdd)[0]
        if re.search('Network', body[i].text_content()):
            bandwidth = comp_tree.xpath('div[@class="body flex"]/span/p')[i].text_content()
    computer = Computer (r3.url, name, price_hr, price_mo, cpus, mem_ram, mem_ssd, bandwidth)
    if (hdd):
        computer.sethdd(hdd_size, hdd_type)
    computer.bandwidth = '(custom)'
    computer.bandwidthtype = 'GB'
    return computer

def extractData():
    if (sqlitedatabase.isTable() == False):
        print("Table not found, creating table...")
        sqlitedatabase.createTable()
    print("Extracting data...")
    makeRequests()
    locations = buildTrees()
    for k in range (0, len(locations)):
        comp = locations[k]
        for i in range (0, len(comp)):
            if k == 0:
                computer = extractR1(comp[i])
            elif k == 1:
                computer = extractR2(comp[i])
            else:
                computer = extractR3(comp[i])
            computer.convertToGB()
            sqlitedatabase.tableInsert(computer.toSQL())

    sqlitedatabase.tableSave()
    print("Data extracted!")
