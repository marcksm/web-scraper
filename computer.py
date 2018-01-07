import re

class Computer:
    def __init__(self, service, name, priceHr, priceMo, cpus, memRam, memSSD, bandwidth):
        self.name = name
        self.service = service
        self.priceHr = re.findall("\d+\.\d+", priceHr)[0]
        self.priceMo = float(re.findall("[0-9]+\.*[0-9]*", priceMo)[0])
        self.cpus = int(re.findall("\d+", cpus)[0])
        self.memRam = float(re.findall("[0-9]+\.*[0-9]*", memRam)[0])
        self.ramtype = re.findall("[a-zA-Z]+", memRam)[0]
        self.memSSD = float(re.findall("[0-9]+\.*[0-9]*", memSSD)[0])
        self.ssdtype = re.findall("[a-zA-Z]+", memSSD)[0]
        self.bandwidth = float(re.findall("[0-9]+\.*[0-9]*", bandwidth)[0])
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


    def toSQL(self):
        data = [self.name, self.service, self.priceHr, self.priceMo, self.cpus, self.memRam, self.memSSD, self.bandwidth]
        return data

    def showData(self):
        print ("Name = ", self.name)
        print ("Price hr = ", self.priceHr)
        print ("Price mo = ", self.priceMo)
        print ("CPUS = ", self.cpus)
        print ("RAM = ", self.memRam)
        print ("RAM = ", self.ramtype)
        print ("SSD = ", self.memSSD)
        print ("SSD = ", self.ssdtype)
        print ("Transfer = ", self.bandwidth)
        print ("Transfer = ", self.bandwidthtype)
