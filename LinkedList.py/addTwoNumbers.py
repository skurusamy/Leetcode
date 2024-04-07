class node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self, node) -> None:
        self.head = node


def addTwoNumbers(l1,l2):
    dummyNode = node(0)
    ptr =  LinkedList(dummyNode)
    head1 = l1.head
    head2 = l2.head
    carry = 0
    res = ptr.head
    if l1 is None and l2 is None:
        return None
    while head1 is not None and head2 is not None:
        sum = head1.val + head2.val + carry
        curNode = node(sum % 10)
        carry = sum // 10
        if res is None:
            res = curNode        
        else:
            res.next = curNode
            res = res.next
        head1 = head1.next
        head2 = head2.next
    while head1 is not None:
        sum = head1.val  + carry
        curNode = node(sum % 10)
        carry = sum // 10
        if res is None:
            res = curNode
            
        else:
            res.next = curNode
            res = res.next
        head1 = head1.next
    while head2 is not None:
        sum = head2.val  + carry
        curNode = node(sum % 10)
        carry = sum // 10
        if res is None:
            res = curNode
        else:
            res.next = curNode
            res = res.next
        head2 = head2.next
    if carry != 0:
        curNode = node(carry)
        res.next = curNode
        res = res.next
    return dummyNode.next
        

def printLinkedList(head):
    if head is None:
        print("No linked List") 
        return
    while head is not None:
        print(head.val, "-> ",end="")
        head = head.next
    print("Null")
    return


node1 = node(2)
node2 = node(4)
node3 = node(1)
node4 = node(9)
node1.next = node2
node2.next = node3
node3.next = node4
l1 = LinkedList(node1)

node5 = node(5)
node6 = node(6)
node7 = node(4)
node8 = node(1)
node5.next = node6
node6.next = node7
node7.next = node8
l2 = LinkedList(node5)

ans = addTwoNumbers(l1,l2)
printLinkedList(l1.head)
printLinkedList(l2.head)
printLinkedList(ans)