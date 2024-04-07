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

def mergeSort(head1,head2):
    dummyHead = LinkedList(node(-999))
    ans = dummyHead
    if head1 is None and head2 is None:
        return None
    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            currNode = node(head1.val)
            head1 = head1.next
        else:
            currNode = node(head2.val)
            head2 = head2.next
        ans.next = currNode
        ans = ans.next
    while head1 is not None:
        currNode = node(head1.val)
        head1 = head1.next
        ans.next = currNode
        ans = ans.next
    while head2 is not None:
        currNode = node(head2.val)
        head2 = head2.next
        ans.next = currNode
        ans = ans.next
    return dummyHead.next

node1 = node(2)
node2 = node(4)
node3 = node(7)
node4 = node(9)
node1.next = node2
node2.next = node3
node3.next = node4
l1 = LinkedList(node1)

node5 = node(1)
node6 = node(3)
node7 = node(5)
node8 = node(6)
node5.next = node6
node6.next = node7
node7.next = node8
l2 = LinkedList(node5)

l3 = LinkedList(node(0))
printLinkedList(l1.head)
printLinkedList(l2.head)

printLinkedList(mergeSort(l1.head,l3.head))