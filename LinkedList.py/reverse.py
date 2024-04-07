class node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self, node):
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

def reverse(l1):
    curr = l1.head
    if l1 is None:
        return None
    prev = None
    while(curr):
        second = curr.next
        curr.next = prev
        prev = curr
        curr = second
    return prev

node1 = node(2)
node2 = node(4)
node3 = node(1)
node4 = node(9)
node1.next = node2
node2.next = node3
node3.next = node4
l1 = LinkedList(node1)
printLinkedList(l1.head)
printLinkedList(reverse(l1))