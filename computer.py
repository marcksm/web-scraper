class Computer:
    def __init__(self, service, name, priceHr, priceMo, cpus, memRam, ramtype, memSSD, ssdtype, bandwidth):
        self.name = name
        self.priceHr = priceHr
        self.priceMo = priceMo
        self.cpus = cpus
        self.memRam = memRam
        self.ramtype = ramtype
        self.memSSD = memSSD
        self.ssdtype = ssdtype
        self.bandwidth = bandwidth
#re.findall("\d+\.\d+",
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

    def setcpus(self, cpus):
        self.cpus = cpus
    def getcpus(self):
        return self.cpus

    def setmemRam(self, memRam):
        self.memRam = memRam
    def getmemRam(self):
        return self.memRam

    def setmemSSD(self, memSSD):
        self.name = memSSD
    def getmemSSD(self):
        return self.memSSD

    def setbandwidth(self, bandwidth):
        self.bandwidth = bandwidth
    def getbandwidth(self):
        return self.bandwidth

    def showData(self):
        print ("Name = ", self.name)
        print ("Price hr = ", self.priceHr)
        print ("Price mo = ", self.priceMo)
        print ("CPUS = ", self.cpus)
        print ("RAM = ", self.memRam)
        print ("SSD = ", self.memSSD)
        print ("Transfer = ", self.bandwidth)
