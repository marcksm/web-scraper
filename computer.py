import re

class Computer:
    def __init__(self, service, name, priceHr, priceMo, cpus, memRam, memSSD, bandwidth):
        self.name = name
        self.service = service
        self.priceHr = re.findall("\d+\.\d+", priceHr)[0]
        self.priceMo = int(re.findall("\d+", priceMo)[0])
        self.cpus = int(re.findall("\d+", cpus)[0])
        self.memRam = int(re.findall("\d+", memRam)[0])
        self.ramtype = re.findall("[a-zA-Z]+", memRam)[0]
        self.memSSD = int(re.findall("\d+", memSSD)[0])
        self.ssdtype = re.findall("[a-zA-Z]+", memSSD)[0]
        self.bandwidth = int(re.findall("\d+", bandwidth)[0])
        self.bandwidthtype = re.findall("[a-zA-Z]+", bandwidth)[0]
    # 
    # def convertTo(storageType):
    #     if !ramtype == storageType:
    #         if ramtype == 'MB':
    #             (FORMULA)
    #         if ramtype == 'TB':
    #             (FORMULA)
    #         if ramtype == 'GB':
    #             (FORMULA)
    #         ramtype = storageType

    def showData(self):
        print ("Name = ", self.name)
        print ("Price hr = ", self.priceHr)
        print ("Price mo = ", self.priceMo)
        print ("CPUS = ", self.cpus)
        print ("RAM = ", self.memRam)
        print ("RAM = ", self.ramtype)
        print ("SSD = ", self.memSSD)
        print ("Transfer = ", self.bandwidth)
        print ("Transfer = ", self.bandwidthtype)
