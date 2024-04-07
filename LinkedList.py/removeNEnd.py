class node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self, node) -> None:
        self.head = node

def printLinkedList(head):
    if head is None:
        print("No linked List") 
        return
    while head is not None:
        print(head.val, "-> ",end="")
        head = head.next
    print("Null")
    return

def delfromLast(l1,n):
    slowptr = l1.head
    fastptr = l1.head
    tracker = n 
    j = 0
    if l1 is None:
        return None
    while fastptr is not None:
        
        fastptr = fastptr.next
        if (tracker - j +1 == 0):
            slowptr = slowptr.next
            tracker += 1
        j += 1
    if slowptr.next is  not None:
        slowptr.next = slowptr.next.next
    else:
        slowptr.next = None
node1 = node(2)
node2 = node(4)
node3 = node(1)
node4 = node(9)
node1.next = node2
node2.next = node3
node3.next = node4
l1 = LinkedList(node1)
printLinkedList(l1.head)
delfromLast(l1,3)
printLinkedList(l1.head)