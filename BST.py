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

def delete(root,val):
    if root is None:
        return
    if root.val == val and root.right is None and root.left is None:
        root = None
        return root
    # just find the node to be deleted and assign its parent
    parent = root
    curr = root
    while curr.val != val:
        parent = curr
        if curr.val > val:
            curr = curr.left
        else:
            curr = curr.right
    # if node has zero child
    if curr.left is None and curr.right is None:
        #check if node is right or left child
        if parent.left == curr:
            parent.left = None
        else:
            parent.right = None
    # if node has one child
        # if it has left child
    if curr.left != None and curr.right == None:
        if parent.left == curr:
            parent.left = curr.left
        else:
            parent.right = curr.left
        # if it has left child
    if curr.right != None and curr.left == None:
        if parent.left ==curr:
            parent.left = curr.right
        else:
            parent.right = curr.right
     # if node has two children
    if curr.left != None and curr.right != None:
        x=findMax(curr)
        curr.val = x
        curr.right = delete(curr.right,x)
    return

def inorder(root):
    if (root == None):
        return
    else:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def preorder(root):
    if (root == None):
        return
    else:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if (root == None):
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")


def getHeight(root):
    h = 0
    if root == None:
        return 0
    if (root.left != None):
        h = 1 + getHeight(root.left)
    if (root.right != None):
        h = 1 + getHeight(root.right)
    return h


def leftViewHelper(root, level, max_level):
    if root == None:
        return
    if (max_level[0] < level):
        print(root.val)
        max_level[0] = level
    leftViewHelper(root.left, level + 1, max_level)
    leftViewHelper(root.right, level + 1, max_level)


def leftView(root):
    max_level = [0]
    leftViewHelper(root, 1, max_level)


def rightViewHelper(root, level, max_level):
    if root == None:
        return
    if (max_level[0] < level):
        print(root.val)
        max_level[0] = level
    rightViewHelper(root.right, level + 1, max_level)
    rightViewHelper(root.left, level + 1, max_level)


def rightView(root):
    max_level = [0]
    leftViewHelper(root, 1, max_level)


'''def levelOrder(root,level):
    if root == None:
        return
    if level == 1:
        print(root.val)
    else:
        levelOrder(root.left,level-1)
        levelOrder(root.right,level-1)
'''


def levelOrder(root):
    if root is None:
        return
    level_num = 0
    q = []
    q.append(root)
    while len(q) > 0:
        print(q[0].val, end=" ")
        node = q.pop(0)

        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)
def kSearch(root, num, maxdist,key):
    if root is None:
        return
    if(num == root.val):
        key[0]=num
        return
    if  maxdist > abs(num-root.val):
        maxdist = abs(num - root.val)
        key[0] = root.val
    if num > root.val:
            kSearch(root.right,num,maxdist,key)
    elif num < root.val:
            kSearch(root.left,num,maxdist,key)

def search(root,key):
    if root is None:
        return
    if root.val == key:
        return root.val
    if key > root.val:
        return search(root.right, key)
    else:
        return search(root.left, key)
    #return False

def chain(root):
        if root is None:
            return
        curr = root
        leftCount=0
        while curr.left!= None:
            leftCount += 1
            curr = curr.left
        curr = root
        rightCount = 0
        while curr.right != None:
            rightCount += 1
            curr = curr.right
        return leftCount + rightCount +1

def findMin(root):
    if root.left != None:
        return findMin(root.left)
    else:
        return root.val

def findMax(root):
    if root.right != None:
        return findMin(root.right)
    else:
        return root.val
def inorderItr(root):
    if root is None:
        return
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.val,end=" ")
            current = current.right
        else:
            break

def lca(root,p,q):
    if root is None:
        return
    if root.val < p and root.val < q:
        return lca(root.right,p,q)
    elif root.val > p and root.val > q:
        return lca(root.left,p,q)
    else:
        return root

def leftView_alt(root):
    if root is None:
        return
    output = []
    queue = [root,]
    while(queue):
        size = len(queue)
        for i in range(size):
            x = queue.pop(0)
            if i == size -1:
                output.append(x.val)  
            if x.right is not None:
                queue.append(x.right)  
            if x.left is not None:
                queue.append(x.left)
        
    return output

def rightView_alt(root):
    if root is None:
        return
    output = []
    queue = [root,]
    while(queue):
        size = len(queue)
        for i in range(size):
            x = queue.pop(0)
            if i == size -1:
                output.append(x.val) 
            if x.left is not None:
                queue.append(x.left) 
            if x.right is not None:
                queue.append(x.right)  
        
        
    return output

# main
root = None
'''\
root = insert(root, 23)
insert(root, 4)
insert(root, 13)
insert(root, 1)
insert(root, 44)
insert(root, 40)
insert(root, 33)
insert(root, 60)
insert(root, 55)
insert(root, 50)
insert(root,65)
insert(root, 2)
'''
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
print("Inorder")
inorder(root)
'''

print("\nPreOrder ")
preorder(root)
print("\nPostOrder ")
postorder(root)
h = getHeight(root)
print("\nHeight: " + str(h))

#print("Level Order: ")
#levelOrder(root)
#Closed node of a given number
num = int(input("\nEnter number to be searched: "))
ans=[-1]
kSearch(root, num,9999999,ans)
print(ans[0])

val = int(input("\nEnter the value to be searched: "))
print(search(root,val))
print()

'''
#delete(root,50)
print("\nLevel Order: ")
levelOrder(root)
'''
print("\nInorder:" )
inorderItr(root)

print(lca(root,67,70).val)
'''

print("\nLeftView: ",leftView_alt(root))
print("\rightView: ",rightView_alt(root))
print(chain(root))