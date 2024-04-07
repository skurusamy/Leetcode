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

    def insertMiddle(self, val, aftEle):
        newNode = node(val)
        if self.head == None:
            self.head = newNode
        else:
            curr = self.head
            while (curr.next != None and curr.data != aftEle):
                curr = curr.next
            if (curr.data == aftEle):
                newNode.next = curr.next
                curr.next = newNode
            else:
                curr.next = newNode

    def delFirst(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next

    def delMiddle(self, ele):
        if self.head == None:
            return
        else:
            curr = self.head
            while (curr.next != None and curr.data != ele):
                prev = curr
                curr = curr.next
            if (curr.next == None):
                return
            else:
                prev.next = curr.next

    def delLast(self):
        if self.head == None:
            return
        else:
            curr = self.head
            while (curr.next != None):
                prev = curr
                curr = curr.next
            prev.next = None
    def reverseList(self):
        curr = self.head
        prev = None
        while curr:
            second = curr.next
            curr.next = prev
            prev = curr
            curr = second
        self.head = prev


def union(head1,head2):
    result = set()
    curr = head1
    while curr!= None:
        result.add(curr.data)
        curr = curr.next
    curr = head2
    while curr!= None:
        if curr.data not in result:
            result.add(curr.data)
        curr = curr.next
    return result

def intersect(head1,head2):
    map = set()
    result =[]
    curr = head1
    while curr != None:
        map.add(curr.data)
        curr = curr.next
    curr = head2
    while curr != None:
        if curr.data in map:
            result.append(curr.data)
        curr = curr.next
    return result
def sorting(l):
    q =[]
    for head in l:
        while(head!=None):
            heapq.heappush(q,head.data)
            head = head.next
    dummy = node(" ")
    newHead = dummy
    for i in range(len(q)):
        newHead.next = node(q.pop(0))
        newHead = newHead.next
    return dummy.next



# main
# first linked list
l = LinkedList()
l.insertFirst(5)
l.insertFirst(4)
l.insertFirst(3)
l.insertFirst(2)
l.insertLast(6)
#l.insertMiddle(6, 1)
#l.delMiddle(2)
#l.delLast()
#l.display()
#l.reverseList()
#l.display()
head1 = l.head
l2 = LinkedList()
l2.insertFirst(30)
l2.insertFirst(20)
l2.insertFirst(11)
l2.insertFirst(3)
#l2.display()
head2 = l2.head
l = [head1,head2]
head3 = sorting(l)
l3 = LinkedList()
l3.head = head3
l3.display()
#print(union(head1,head2))
#print(intersect(head1,head2))

l3.display()
l3.reverseList()


