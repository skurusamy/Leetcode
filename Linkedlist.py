class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self,node):
        self.head = node

    def insertAtEnd(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = node
        return 
    def printLinkedlist(self):
        if self.head is None:
            print
        curr = self.head
        while(curr):
            print(curr.data,end=" -> ")
            curr = curr.next
        print("None")
        
    def reverse(self):
        if self.head is None:
            return
        prev = None
        curr = self.head
        sec = None
        while curr:
            sec = curr.next
            curr.next = prev
            prev = curr
            curr = sec
        self.head =  prev

node1 = Node(1)
ll = LinkedList(node1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)
ll.insertAtEnd(5)
ll.printLinkedlist()
ll.reverse()
ll.printLinkedlist()
