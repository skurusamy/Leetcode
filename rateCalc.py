from collections import defaultdict

class Shipments:
    def __init__(self):
        self.shipment = defaultdict(dict)
    
    def addShipment(self, id, weight, volume,crewSize,rate):
        if id not in self.shipment.keys():
            self.shipment[id]["weight"] = weight
            self.shipment[id]["volume"] = volume
            self.shipment[id]["crewSize"] = crewSize
            self.shipment[id]["rate"] = rate

    def calcRatebasedonWeight(self,id):
        if id not in self.shipment.keys():
            return -1
        return self.shipment[id]["weight"] * self.shipment[id]["rate"]
    def calcRateBasedOnVolume(self,id):
        if id not in self.shipment.keys():
            return -1
        price = 0
        if self.shipment[id]["volume"] < 10:
            price = self.shipment[id]["volume"] * 9
        elif self.shipment[id]["volume"] > 10 and self.shipment[id]["volume"] < 50:
            price = self.shipment[id]["volume"] * 5
        elif self.shipment[id]["volume"] >= 50:
            price = self.shipment[id]["volume"] * 4
        return price



s = Shipments()
s.addShipment(1,20,100,5,5)
s.addShipment(2,20,40,5,7)
s.addShipment(3,10,45,6,9)
print(s.shipment)
for i in s.shipment.keys():
    print(f'Volume {s.shipment[i]["volume"]} is {s.calcRateBasedOnVolume(i)}')