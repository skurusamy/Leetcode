class node:
    def __init__(self, val):
        self.val = val
        self.left= None
        self.right=None
class CDLL:
    def __init__(self,val):
        self.data = val
        self.prev = None
        self.next = None
def toBT(l,parent,child,n):
    if child < n :
        childNode = node(l[child])
        parent = childNode
        parent.left = toBT(l,parent.left,(2*child)+1,n)
        parent.right = toBT(l,parent.right,(2*child)+2,n)
    return parent
def levelOrder(root):
    if root is None:
        return
    q=[]
    ans =[]
    q.append(root)
    ans.append(root.val)
    while(len(q)>0):
       # print(q[0].val)
        curr = q.pop(0)
        if(curr.left is not None):
            q.append(curr.left)
            ans.append(curr.left.val)
        if curr.right is not None:
            q.append(curr.right)
            ans.append(curr.right.val)
    return ans
def createLinkedList(l,head,tail):
    for i in range(len(l)):
        newNode = CDLL(l[i])
        if head is None:
            head = newNode
            tail = newNode
        else:
            previ  = tail
            tail.next = newNode
            newNode.prev = previ
            newNode.next = head
            tail = newNode
            head.prev = tail
    return head,tail


def printLinkedList(head,tail):
    if(head is None):
        return
    curr = head
    while curr.next != head:
        print(curr.data,end="")
        curr=curr.next
    print(curr.data,end="")
    curr = tail
    print()
    while curr.prev != tail:
        print(curr.data,end="")
        curr = curr.prev
    print(curr.data,end="")


def altLevelOrder(root):
    if root is None:
        return None
    q= []
    q.append(root)
    while len(q) > 0:
        print(q[0].val,end=" ")
        curr = q.pop(0)
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)

l = [1,3,2,6,7,8]
ans=[]
root = None
root= toBT(l,root,0,len(l))
#altLevelOrder(root)
ans = levelOrder(root)
print("Level Order:"+str(ans))
head = None
tail = None
head,tail = createLinkedList(ans,head,tail)
print("LinkedList: ")
printLinkedList(head,tail)
