class Node:
    def __init__(self,val) -> None:
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insertAtFirst(self,ele):
        newNode  = Node(ele)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def insertAtMiddle(self,ele,afterEle):
        newNode = Node(ele)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            prev = cur
            while(cur.data != afterEle and cur is not None):
                cur = cur.next
            if cur.data == afterEle:
                newNode.next = cur.next
                cur.next = newNode

    def insertAtEnd(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head 
            while(cur.next):
                cur = cur.next 
            cur.next = newNode         

    def deleteANode(self,ele):
        if self.head is None:
            print('no nodes to delete')
            return
        if self.head.data == ele:
            self.head = self.head.next
            return
        cur = self.head
        while cur is not None and cur.data != ele:
            prev = cur
            cur = cur.next
        if cur.data == ele:
            prev.next = cur.next 

    def print(self):
        cur = self.head
        while(cur):
            print(cur.data,end= " -> ")
            cur = cur.next
        print("NONE\n")

    #with buffer
    def withbufferRemoveDup(self):
        if self.head is None:
            return
        LinkedList_set = set()
        cur = self.head
        prev = None
        while(cur):
            if (cur.data not in LinkedList_set):
                LinkedList_set.add(cur.data)
                prev = cur
                cur = cur.next
            else:
                prev.next = cur.next
                cur = cur.next

    def withoutbufferRemoveDup(self): # 2 loops o(n2)
        if self.head is None:
            return
        cur = self.head
        while(cur):
            nextNode = cur
            while(nextNode):
                if cur.data == nextNode.data:
                    nextNode.next = nextNode.next.next
                nextNode = nextNode.next
            cur = cur.next
    def kfromLastIter(self,k):
        if self.head is None:
            return
        temp1 = self.head
        temp2 = self.head
        for i in range(k):
            temp1 = temp1.next
        while(temp1):
            temp1 = temp1.next
            temp2 = temp2.next
        return temp2.data

    def partition(self,x):
        if self.head is None:
            return
        newList = LinkedList()
        cur = self.head
        while(cur):
            if cur.data >= x:
                newList.insertAtEnd(cur.data)
            else:
                newList.insertAtFirst(cur.data)
            cur = cur.next
        newList.print()

    def reverse(self):
        if self.head is None:
            return
        temp1 = None
        cur = self.head
        while(cur):
            newNode = cur.next
            cur.next =  temp1
            temp1 = cur
            cur = newNode
        self.head = temp1
    def palindrome(self):
        if self.head is None:
            return
        slow = self.head
        fast = self.head
        stack =[]
        while (fast != None and fast.next != None):
            stack.append(slow.data)
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        while(slow):
            x = stack.pop()
            if x != slow.data:
                return False
            slow = slow.next
        return True

ll = LinkedList()
'''
ll.insertAtFirst(5)
ll.insertAtFirst(4)
ll.insertAtMiddle(3,4)
ll.insertAtFirst(1)
ll.insertAtFirst(10)
ll.insertAtFirst(3)
ll.insertAtEnd(10)
ll.insertAtEnd(2)
#ll.deleteANode(1)
#ll.partition(4)# partitioning elements less than x in from=nt greater than that at back

ll.insertAtFirst(1)
ll.insertAtEnd(10)
ll.insertAtFirst(2)
ll.insertAtFirst(2)
ll.insertAtFirst(1)
print(ll.palindrome())
ll.print()
ll.reverse()
ll.print()
#print(ll.kfromLastIter(5))
#ll.withbufferRemoveDup()
#ll.print()



# add two numbers that ares stored in linkedlist: -- the digit is in reverse order
def sum(l1,l2):
    ans = LinkedList()
    head1 = l1.head
    head2 = l2.head
    carry = 0
    while(head1 != None and head2 != None):
        sumVal = (head1.data + head2.data + carry ) %10
        carry = (head1.data + head2.data + carry ) // 10
        ans.insertAtEnd(sumVal)    
        head1 = head1.next
        head2 = head2.next
    while(head1):
        sumVal = (head1.data + 0 + carry ) %10
        carry = (head1.data + 0 + carry ) // 10
        ans.insertAtEnd(sumVal)    
        head1 = head1.next
    while(head2):
        sumVal = (head2.data + 0 + carry ) %10
        carry = (head2.data + 0 + carry ) // 10
        ans.insertAtEnd(sumVal)    
        head2 = head2.next
    ans.print()
'''
def intersection(l1,l2):
    if l1 is not None and l2 is not None:
        map = set()
        resultList = LinkedList()
        cur1 = l1.head
        while(cur1):
            map.add(cur1.data)
            cur1 = cur1.next
        cur2 = l2.head
        while(cur2):
            if cur2.data in map:
                resultList.insertAtEnd(cur2.data)
            cur2 = cur2.next
        resultList.print()

def union(l1,l2):
    if l1 is not None and l2 is not None:
        map = set()
        resultList = LinkedList()
        cur1 = l1.head
        while(cur1):
            map.add(cur1.data)
            resultList.insertAtEnd(cur1.data)
            cur1 = cur1.next
        cur2 = l2.head
        while(cur2):
            if cur2.data not in map:
                resultList.insertAtEnd(cur2.data)
            cur2 = cur2.next
        resultList.print()

l1 = LinkedList()
l1.insertAtEnd(5)
l1.insertAtFirst(4)
l1.insertAtFirst(3)
l1.insertAtFirst(2)
l1.insertAtFirst(7)
l1.insertAtFirst(7)

l2 = LinkedList()
l2.insertAtEnd(6)

l2.insertAtFirst(8)
l2.insertAtFirst(7)
#l2.insertAtFirst(1)
l1.print()
l2.print()
#sum(l1,l2)
intersection(l1,l2)
union(l1,l2)

ll.withbufferRemoveDup()
