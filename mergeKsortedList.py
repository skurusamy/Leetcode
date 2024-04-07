import heapq
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self, val):
        newNode = node(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertLast(self, val):
        newNode = node(val)
        if self.head == None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newNode

    def display(self):
        curr = self.head
        if (self.head == None):
            print(self.head.data,end=" ")
        else:
            while (curr != None):
                print(curr.data,end=" ")
                curr = curr.next
        print()
def mergeKsortedList(ip):
    minHeap =[]
    heapq.heapify(minHeap)
    for i in range(len(ip)):
        while(ip[i].head != None):
            heapq.heappush(minHeap,ip[i].head.data)
            ip[i].head= ip[i].head.next
    #heapq.heapify(minHeap)
    print(minHeap)
    dummy = LinkedList()
    while(minHeap):
        dummy.insertLast(heapq.heappop(minHeap))
    dummy.display()

l = LinkedList()
l.insertFirst(15)
l.insertFirst(13)
l.insertFirst(1)
#l.display()

l1 = LinkedList()
l1.insertFirst(16)
l1.insertFirst(14)
l1.insertFirst(3)
l1.insertFirst(2)
#l1.display()

l2 = LinkedList()
l2.insertFirst(6)
l2.insertFirst(5)
#l2.display()

ip = []
ip.append(l)
ip.append(l1)
ip.append(l2)

mergeKsortedList(ip)