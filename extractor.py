import requests
from lxml import html
from computer import Computer
import sqlitedatabase
import re
import string
import random

global stack
""" stack is responsable to store all information in order from the selected computer html DIV """
stack = []

def makeRequests():
    """ This function make request to the selected websites and return a list with them """
    r1 = requests.get('https://www.digitalocean.com/pricing/')
    r2 = requests.get('https://www.vultr.com/pricing/')
    r3 = requests.get('https://www.packet.net/bare-metal/')
    r4 = requests.get('https://www.vultr.com/pricing/dedicatedcloud/')
    service = [r1, r2, r3,r4]
    return service

def name_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """ This function generates a random name using 6 charactes, this is used for sites that
        do not give a name to a computer
     """
    return ''.join(random.choice(chars) for _ in range(size))

def buildTrees(websites):
    """ This function receives a list of websites and build a tree using xpath and returns it """
    tree1 = html.fromstring(websites[0].text)
    tree2 = html.fromstring(websites[1].text)
    tree3 = html.fromstring(websites[2].text)
    tree4 = html.fromstring(websites[3].text)
    location1 = tree1.xpath('//div[@class="PriceBlock-container"]')
    location2 = tree2.xpath('//div[@class="packages-row row"]/div[@class="col-sm-3 col-xs-6"]')
    location3 = tree3.xpath('//article[@class="pricing-item col-3"]')
    location4 = tree4.xpath('//div[@class="packages-row row"]/div[@class="col-sm-3 col-xs-6"]')
    locations = [location1, location2, location3, location4]
    return locations

def exploreDiv(root):
    """ This function receives a xpath node and explores in order left to right (first to last) until
        find the deepest node with data, then store the data in the global stack
     """
    for i in range (0, len(root)):
        exploreDiv(root[i])
    if root.xpath('@data-hourly'):
        stack.append(root.xpath('@data-hourly')[0] + '/hr')
        stack.append(root.xpath('@data-monthly')[0] + '/mo')
    if (len(root) <= 1 and str(root) != "<!-- /.package -->"):
        div_data = root.text_content()
        div_data = re.sub('\s+',' ',div_data)
        stack.append(div_data.strip())

def buildComputer(div_itens, service):
    """ This function receives a html DIV from the global stack and a website, and extract the
        computer data using regex and return a Computer class with that data
     """
    div = (' '.join(div_itens)).replace('\n', ' ').replace('\r', '')
    price_mo = re.search("[\$][\s]*[0-9]+[\.*[0-9]*]*[\s]*[/][\s]*[m][o][n]*", div).group()
    price_hr = re.search("[\$][\s]*[0-9]+[\.*[0-9]*]*[\s]*[/][\s]*[h][r|o][u]*", div).group()
    mem_ram = re.search("[0-9]+\.*[0-9]*[\s]*[M|G|T][B][\s]*[a-zA-Z0-9- ]*[\s]*[M|R][e|A][m|M]", div).group()
    cpu = re.search("[0-9]+[\s]*[a-zA-Z]*[\s]*[v|C]*[C|o][P|r][Ue][s]*", div).group()
    mem_ssd = re.search("[0-9]+\.*[0-9]*[\s]*[X]*[\s]*[0-9]+[\s]*[G][B][\s]*[a-zA-Z ]*[\s]*[S][S][D]", div).group()
    bandwidth = re.search("[0-9]+\.*[0-9]*[\s]*[\.*[0-9]*]*[G|T|M][B][\s*][B|T][a|r][n|a][d|n][w|s][i|f][d|e][t|r][h]*", div)
    name = re.search("[u][r][\s]*[A-Z][a-zA-Z0-9]*[\s]*[a-zA-Z0-9 /]*", div)
    hdd = re.search("[0-9]+\.*[0-9]*[\s]*[\.*[0-9]*]*[G|T|M][B][\s*][[a-zA-Z ]*[\s]*]*[H][D][D]", div)
    name = (name.group() if name else 'PC_' + name_generator())
    bandwidth = (bandwidth.group() if bandwidth else "0GB")
    computer = Computer (service, name, price_hr, price_mo, cpu, mem_ram, mem_ssd, bandwidth)
    computer.sethdd(hdd.group()) if hdd else 0
    return computer


def extractData():
    """ This is a main function that download and extract data from the requested websites
        and stores it into SQlite database
     """
    if (sqlitedatabase.isTable() == False):
        print("Table not found, creating table...")
        sqlitedatabase.createTable()
    print("Extracting data...")
    websites = makeRequests()
    locations = buildTrees(websites)
    for k in range (0, len(locations)):
        div_comp = locations[k]
        for i in range (0, len(div_comp)):
            stack.clear()
            exploreDiv(div_comp[i])
            computer = buildComputer(stack, websites[k].url)
            computer.convertToGB()
            sqlitedatabase.tableInsert(computer.toSQL())
    sqlitedatabase.tableSave()
    print("Data extracted!")
