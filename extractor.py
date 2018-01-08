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
    global service, r1, r2, r3
    r1 = requests.get('https://www.digitalocean.com/pricing/')
    r2 = requests.get('https://www.vultr.com/pricing/')
    r3 = requests.get('https://www.packet.net/bare-metal/')
    service = [r1, r2, r3]
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

def buildComputer(div_itens, service):
    div = (' '.join(div_itens)).replace('\n', ' ').replace('\r', '')
    price_mo = re.search("[\$][\s]*[0-9]+[\.*[0-9]*]*[\s]*[/][\s]*[m][o][n]*", div).group()
    price_hr = re.search("[\$][\s]*[0-9]+[\.*[0-9]*]*[\s]*[/][\s]*[h][r|o][u]*", div).group()
    mem_ram = re.search("[0-9]+\.*[0-9]*[\s]*[M|G|T][B][\s]*[a-zA-Z0-9- ]*[\s]*[M|R][e|A][m|M]", div).group()
    cpu = re.search("[0-9]+[\s]*[a-zA-Z]*[\s]*[v|C]*[C|o][P|r][Ue][s]*", div).group()
    mem_ssd = re.search("[0-9]+\.*[0-9]*[\s]*[\.*[0-9]*]*[G|T|M][B][\s*][[a-zA-Z ]*[\s]*]*[S][S][D]", div).group()
    bandwidth = re.search("[0-9]+\.*[0-9]*[\s]*[\.*[0-9]*]*[G|T|M][B][\s*][B|T][a|r][n|a][d|n][w|s][i|f][d|e][t|r][h]*", div)
    name = re.search("[u][r][\s]*[A-Z][a-zA-Z0-9]*[\s]*[a-zA-Z0-9 /]*", div)
    hdd = re.search("[0-9]+\.*[0-9]*[\s]*[\.*[0-9]*]*[G|T|M][B][\s*][[a-zA-Z ]*[\s]*]*[H][D][D]", div)
    name = (name.group() if name else 'PC_' + name_generator())
    bandwidth = (bandwidth.group() if bandwidth else "0GB")
    computer = Computer (service, name, price_hr, price_mo, cpu, mem_ram, mem_ssd, bandwidth)
    computer.sethdd(hdd.group()) if hdd else 0
    return computer

def exploreDiv(root):
    for i in range (0, len(root)):
        exploreDiv(root[i])
    if root.xpath('@data-hourly'):
        stack.append(root.xpath('@data-hourly')[0] + '/hr')
        stack.append(root.xpath('@data-monthly')[0] + '/mo')
    if (len(root) <= 1 and str(root) != "<!-- /.package -->"):
        div_data = root.text_content()
        div_data = re.sub('\s+',' ',div_data)
        stack.append(div_data.strip())

def extractData():
    if (sqlitedatabase.isTable() == False):
        print("Table not found, creating table...")
        sqlitedatabase.createTable()
    print("Extracting data...")
    makeRequests()
    locations = buildTrees()
    for k in range (0, len(locations)):
        div_comp = locations[k]
        for i in range (0, len(div_comp)):
            stack.clear()
            exploreDiv(div_comp[i])
            computer = buildComputer(stack, service[k].url)
            computer.convertToGB()
            sqlitedatabase.tableInsert(computer.toSQL())
    sqlitedatabase.tableSave()
    print("Data extracted!")
