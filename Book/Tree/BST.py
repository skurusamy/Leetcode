class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    newNode = node(val)
    if root == None:
        root = newNode
    else:
        if root.val > newNode.val:
            root.left = insert(root.left, val)
        if root.val < newNode.val:
            root.right = insert(root.right, val)
    return root

def levelOrder(root):
    if root is None:
        return
    q = []
    q.append(root)
    while(q):
        cur=q.pop(0)
        print(cur.val,end=" ")
        if cur.left is not None:
            q.append(cur.left)
        if cur.right is not None:
            q.append(cur.right)

def rightView(root):
    if root is None:
        return
    q =[]
    rightViewNode=[]
    q.append(root)
    while(q):
        size = len(q)
        for i in range(size):
            cur = q.pop(0)
            if i == size-1:
                rightViewNode.append(cur.val)
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
    return rightViewNode

def leftView(root):
    if root is None:
        return
    q = []
    leftViewNode = []
    q.append(root)
    while(q):
        for i in range(len(q)):
            cur = q.pop(0)
            if i == 0:
                leftViewNode.append(cur.val)
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
    return leftViewNode  

def pathsum(root,val):
    if root is None:
        return False
    if root.left is None and root.right is None and val - root.val ==0:
        return True
    else:
        return pathsum(root.left,val- root.val) or pathsum(root.right, val-root.val)

        

root = None
root = insert(root,50)
insert(root,69)
insert(root,45)
insert(root,40)
insert(root,47)
insert(root,39)
insert(root,33)
insert(root,67)
insert(root,72)
insert(root,70)
print("LevelOrder:")
levelOrder(root)
print("\nRightView:",rightView(root))
print("LeftView:",leftView(root))
print("FindPathSum",pathsum(root,140))