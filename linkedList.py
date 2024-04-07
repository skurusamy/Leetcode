class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        return self.head

    def printLL(self):
        if self.head is None:
            return
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
        return
    def reverse(self):
        if self.head is None:
            return
        curr = self.head
        prev = None
        while curr:
            second = curr.next
            curr.next = prev
            prev = curr
            curr = second
        self.head = prev
    def findKth(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseK(self,k):
        dummyNode = Node(-1)
        dummyNode.next = self.head
        lastEle = dummyNode

    
        while True:
            kth = self.findKth(lastEle,k)
            if not kth:
                break 
            k_next = kth.next
            #reversing
            curr = lastEle.next
            prev = kth.next
            while curr != k_next:
                second = curr.next
                curr.next = prev
                prev = curr
                curr = second
            
            tmp = lastEle.next
            lastEle.next = kth
            lastEle = tmp
        return dummyNode.next



l = LinkedList()
l.insert(1)
l.insert(2)
l.insert(4)
l.insert(6)
#l.reverse()

l.reverseK(2)
l.printLL()
