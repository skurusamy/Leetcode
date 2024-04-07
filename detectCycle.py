from platform import node


class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self,node):
        self.head = node

    def printLinkedList(self):
        if self.head is None:
            return
        else:
            cur = self.head
            while(cur):
                print(cur.data,end=' ->')
                cur = cur.next
            print("None")

    def detectCycle(self):
        if self.head is None:
            return
        fast = self.head
        slow = self.head
        while fast != None and fast.next != None  :
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    def countNodes(self,slow):
        curr = slow
        count = 1
        while curr.next != slow:
            count += 1
            curr = curr.next
        return count
    def countCycleNodes(self):
        count = 0
        if self.head is None:
            return
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                count = self.countNodes(slow)
                break
        return  count
    def firstNode(self,node_count):
        if self.head is None:
            return
        ptr1 = self.head
        ptr2 = self.head
        while node_count != 0:
            ptr1 = ptr1.next
            node_count -= 1
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1.data


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

l = LinkedList(node1)
print("Cycle: ",l.detectCycle())
node_count = l.countCycleNodes()
print("Count of nodes in cycle: ", node_count)
print("FirstNode: ", l.firstNode(node_count))

#l.printLinkedList()