class Computer:
    def __init__(self, name, priceHr, priceMo, cpus, memRam, memSSD, bandwidth):
        self.name = name
        self.priceHr = priceHr
        self.priceMo = priceMo
        self.cpus = cpus
        self.memRam = memRam
        self.memSSD = memSSD
        self.bandwidth = bandwidth

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setpriceHr(self, priceHr):
        self.priceHr = priceHr
    def getpriceHr(self):
        return self.priceHr

    def setpriceMo(self, name):
        self.priceMo = priceMo
    def getpriceMo(self):
        return self.priceMo


a = Computer('PC1', 323, 323, 5, 321321, 321321, 3213213)

print (a.getName())
