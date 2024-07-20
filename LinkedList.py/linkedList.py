class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtLast(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = node
        return 
    def printLinkedList(self):
        if self.head is None:
            return
        else:
            cur = self.head
            while(cur):
                print(cur.data,end=' ->')
                cur = cur.next
            print("None")
    def search(self,val):
        if self.head is None:
            return False
        cur = self.head
        while(cur and cur.data != val):
            cur = cur.next
        if cur is None:
            return False
        return True
    def insertAtFirst(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        node.next = self.head 
        self.head = node
        return 
    def insertInMiddle(self,val, pos):
        node = Node(val)
        if self.head is Node:
            return False
        cur = self.head
        while cur and cur.data != pos:
            cur = cur.next
        if(not cur):
            return False
        node.next = cur.next
        cur.next = node
        return True
    def reverse(self):
        if self.head is None:
            return
        cur = self.head
        prev = None
        while cur:
            sec = cur.next
            cur.next = prev
            prev = cur
            cur = sec 
        self.head = prev
        return False
    def findMiddle(self):
        if self.head is None:
            return
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    def findPalindrome(self):
        if self.head is None:
            return
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        #reverse logic
        curr = slow
        sec = slow
        prev = None
        while curr:
            sec = curr.next
            curr.next = prev
            prev = curr
            curr = sec
        slow = prev
        self.printLinkedList()
        ptr = self.head
        while ptr is not None and slow is not None and ptr.data == slow.data:
            ptr = ptr.next
            slow = slow.next 
        if ptr is None and slow is  None:
            return True
        else:
            return False
        return True
        

l = LinkedList()
l.insertAtLast(1)
l.insertAtLast(2)
l.insertAtLast(3)
l.insertAtLast(4)
l.insertAtLast(3)
l.insertAtLast(2)
print(l.search(6))
l.insertAtLast(11)
#l. insertInMiddle(11,3)
#l.reverse()
l.printLinkedList()
#print("Middle Element: ", l.findMiddle())
print("Palindrome ",l.findPalindrome())
#l.printLinkedList()


