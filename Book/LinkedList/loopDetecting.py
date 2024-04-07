class Node:
    def __init__(self,val) -> None:
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def detectLoop(self):
        if self.head is None:
            return
        slow = self.head
        fast = self.head
        while(fast.next is not None and fast.next.next is not None):
            fast = fast.next.next
            slow = slow.next
            if(fast.data == slow.data):
                break
        if fast.next is None or fast.next.next is None:
            print("No loop")
            return
        slow = self.head
        while(slow.data != fast.data):
            slow = slow.next
            fast = fast.next
        print(slow.data)
        return

ll = LinkedList()
# 1-> 2-> 3-> 5->3
n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3
ll.head = n1
ll.detectLoop()