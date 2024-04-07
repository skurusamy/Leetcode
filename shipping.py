from collections import defaultdict
class ShippingYard:
    def __init__(self):
        self.container_id = {}
    def addContainers(self, id, count):
        if id in self.container_id:
            self.container_id[id] += count
            return 
        self.container_id[id] = count
    def removeContainer(self,id,count):
        if id in self.container_id:
            self.container_id[id] -= count
            return
        return -1

class OrderBook:
    def __init__(self):
        self.orders = defaultdict(list)
    
    def order(self,order_id, container_id, order_type, quantity, price):
        self.orders[order_id].append(container_id)
        self.orders[order_id].append(order_type)
        self.orders[order_id].append(quantity)
        self.orders[order_id].append(price)


s= ShippingYard()
s.addContainers(1,10)
s.addContainers(2,20)
print(s.removeContainer(3,1))
print(s.container_id)

o = OrderBook()
o.order(1,1,"Buy",1,20)

