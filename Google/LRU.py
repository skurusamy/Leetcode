class Node:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.curSize = 0
        self.head = Node(-1,-1)

    def insertAtFirst(self,node):
        if self.head.next == None:
            self.head.next = node
            node.prev = self.head
        else:
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
    def printCache(self):
        if self.head.next is None:
            return None
        cur = self.head.next
        while(cur):
            print(cur.key,cur.value,end="->")
            cur = cur.next
        print("Null")

    def deleteLastNode(self):
        if self.head.next is None:
            return None
        cur = self.head.next
        while(cur.next):
            previous = cur
            cur = cur.next
        previous.next = None
   
    def put(self, key, value):
        newNode = Node(key,value)
        if self.curSize < self.capacity:
            self.insertAtFirst(newNode)
            self.curSize += 1
        else:
            self.deleteLastNode()
            self.insertAtFirst(newNode)
        return 
    def get(self,key):
        if self.curSize == 0:
            return -1
        cur = self.head.next
        while(cur.next and cur.key != key):
            previous = cur
            cur = cur.next
        if(cur.key == key):
            node = cur
            previous.next = cur.next
            if cur.next is not None:
                cur.next.prev = previous
            self.insertAtFirst(node)
            return key
        if(cur.next is None):
            return -1

        
        
c = Cache(2)
c.put(1,1)
c.put(2,2)
c.put(3,3)
print(c.get(1))
print(c.get(2))
c.printCache()
        


