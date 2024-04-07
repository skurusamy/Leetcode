import datetime
import random
import time
class Ticket:
    def __init__(self,vNo,vtype,slot) -> None:
        self.vehicleNo = vNo
        self.vehicleType = vtype
        self.entryTime = datetime.datetime.now()
        self.slotNo = slot
        self.amount  = 0
        

class ParkingSlot:
    def __init__(self,size) -> None:
        self.filledSlot = []
        self.capacity = size
        self.ticketDetails =[]
    def assignSlot(self,num,type):
        while True:
            slot = random.randrange(0,self.capacity)
            if slot not in self.filledSlot:
                t = Ticket(num,type,slot)
                self.filledSlot.append(slot)
                self.ticketDetails.append(t)
                return t

    def printTicket(self,t):
        print("Ticket Details")
        print("**************")
        print(t.vehicleNo)
        print(t.vehicleType)
        print(t.entryTime)
        print(t.slotNo)
        print(t.amount)
        print("-----------------------------Thank you!---------")

    def exit(self,t):
        exitTime = datetime.datetime.now()
        time = exitTime - t.entryTime
        time = time.total_seconds()
        amount = 10 * time
        index = self.filledSlot.index(t.slotNo)
        self.filledSlot.pop(index)
        t.amount = amount
        return amount

    def printAllTickets(self):
        for i in range(len(self.ticketDetails)):
            self.printTicket(self.ticketDetails[i])

p = ParkingSlot(10)
t1 = p.assignSlot("TN 123","bicycle")
t2 = p.assignSlot("TN 23","car")
p.printTicket(t1)
time.sleep(5)
p.exit(t1)
p.printAllTickets()



