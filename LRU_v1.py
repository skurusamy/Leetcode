class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.length = 0
        

    def get(self, key: int) -> int:
        res = self.deleteNode(key)
        if res != -1:
            self.insertFirst(key,res)
        self.printLinkedList()
        return res

    def put(self, key: int, value: int) -> None:
        if self.findNode(key):
            self.deleteNode(key)
        self.insertFirst(key,value)
        if self.length > self.capacity:
            self.deleteLast()
        self.printLinkedList()

    def findNode(self,key):
        if self.head is None:
            return False
        curr = self.head
        while curr.next and curr.key != key:
            curr = curr.next
        if curr.key == key:
            return True
        return False
        
    def insertFirst(self, key, value):
        newNode = Node(key,value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
    def printLinkedList(self):
        print("In print")
        curr = self.head
        while curr:
            print(curr.key,curr.value)
            curr = curr.next

    def deleteLast(self):
        if self.head is None:
            return
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
    def deleteNode(self,key):
        if self.head is None:
            return -1
        res = -1
        curr = self.head
        if curr.key == key:
            res = curr.value
            self.head = curr.next
            curr.next = None
            self.length -= 1
            return res
        
        while curr.next and curr.key != key :
            prev = curr
            curr = curr.next
        if curr.key == key:
            res = curr.value
            prev.next = curr.next
            self.length -= 1
        return res


    
    

        
        

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.get(2)
obj.put(2,6)
obj.get(1)
obj.put(1,5)
obj.put(1,2)
obj.get(1)
obj.get(2)
