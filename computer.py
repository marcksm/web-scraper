import re

class Computer:
    """ This class is responsable to store a computer data givem parametes """
    hdd = None
    hdd_size = None
    hdd_type = None

    def __init__(self, service, name, priceHr, priceMo, cpus, memRam, memSSD, bandwidth):
        self.name = re.findall("[A-Z][a-zA-Z0-9_]*[\s]*[a-zA-Z0-9 /]*", name)[0]
        self.service = service
        self.priceHr = re.findall("\d+\.\d+", priceHr)[0]
        self.priceMo = float(re.findall("[0-9]+\.*[0-9]*", priceMo)[0])
        self.cpus = int(re.findall("\d+", cpus)[0])
        self.memRam = float(re.findall("[0-9]+\.*[0-9]*", memRam)[0])
        self.ramtype = re.findall("[a-zA-Z]+", memRam)[0]
        self.bandwidth = float(re.findall("[0-9]+\.*[0-9]*", bandwidth)[0])
        self.bandwidthtype = re.findall("[a-zA-Z]+", bandwidth)[0]
        if ("X" in memSSD):
            mult = memSSD.split(" ")[0]
            value = memSSD.split(" ")[2]
            self.ssdtype = memSSD.split(" ")[3]
            self.memSSD = float (float(mult) * float(value))
        else:
            self.memSSD = float(re.findall("[0-9]+\.*[0-9]*", memSSD)[0])
            self.ssdtype = re.findall("[a-zA-Z]+", memSSD)[0]
        if (self.bandwidth == 0):
            self.bandwidth = "(custom)"

    def ishdd(self):
        """ Returns true if this computer has HDD """
        if hdd != None:
            return True
        else:
            return False

    def sethdd(self, string):
        """ Set a HDD to this computer """
        self.hdd = True
        self.hdd_size = float(re.findall("[0-9]+\.*[0-9]*", string)[0])
        self.hdd_type = re.findall("[a-zA-Z]+", string)[0]
        if (self.ssdtype == 'GB'):
            if (self.hdd_type == 'TB'):
                self.hdd_size = float(self.hdd_size * 1024)
                self.hdd_type = 'GB'
        if (self.ssdtype == 'TB'):
            if (self.hdd_type == 'GB'):
                self.hdd_size = float(self.hdd_size / 1024)
                self.hdd_type = 'GB'
        self.memSSD = self.memSSD + self.hdd_size

    def convertToGB(self):
        """ Convert RAM, SSD, HDD, bandwidth formats to GB """
        if self.ramtype != 'GB':
            if self.ramtype == 'MB':
                self.memRam = float(self.memRam/1024)
            if self.ramtype == 'TB':
                self.memRam = float(self.memRam*1024)
            self.ramtype = 'GB'
        if self.ssdtype != 'GB':
            if self.ssdtype == 'MB':
                self.memSSD = float(self.memSSD/1024)
            if self.ssdtype == 'TB':
                self.memSSD = float(self.memSSD*1024)
            self.ssdtype = 'GB'
        if self.bandwidthtype != 'GB':
            if self.bandwidthtype == 'MB':
                self.bandwidth = float(self.bandwidth/1024)
            if self.bandwidthtype == 'TB':
                self.bandwidth = float(self.bandwidth*1024)
            self.bandwidthtype = 'GB'


    def toSQL(self):
        """ Prepare and return a list to be used in SQlite script to insert in db """
        data = [self.name, self.service, self.priceHr, self.priceMo, self.cpus, self.memRam, self.memSSD, self.bandwidth]
        return data

    def showData(self):
        """ Debug function """
        print ("Name = ", self.name)
        print ("Price hr = ", self.priceHr)
        print ("Price mo = ", self.priceMo)
        print ("CPUS = ", self.cpus)
        print ("RAM = ", self.memRam)
        print ("RAM TYPE= ", self.ramtype)
        print ("SSD = ", self.memSSD)
        print ("SSD TYPE = ", self.ssdtype)
        print ("Transfer = ", self.bandwidth)
        print ("Transfer TYPE = ", self.bandwidthtype)
