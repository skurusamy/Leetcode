class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root,val):
        newNode = node(val)
        if root is None:
            root = newNode
        else:
            if root.val >  val:
                root.left = insert(root.left, val)
            else:
                root.right = insert(root.right, val)
        return root

def insertItr(root, val):
    newNode = node(val)
    if root is None:
        root = newNode
    else:
        cur = root
        while(cur):
            if cur.val < val and cur.right is not None:
                cur = cur.right
            elif cur.val > val and cur.left is not None:
                cur = cur.left
            else:
                break
        if cur.val < val:
            cur.right = newNode
        else:
            cur.left = newNode
    return root
                

def levelOrder(root):
    if root is None: return root
    queue =[root,]
    while(queue):
        x = queue.pop(0)
        if x.left is not None:
            queue.append(x.left)
        if x.right is not None:
            queue.append(x.right)
        print(x.val,end=" ")
    print()
        
def inorder(root):
    if root is None: return None
    if(root):
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorderItr(root):
    if root is None:
        return None
    stack = [root,]
    while(stack):
        x = stack.pop()
        if x.right is not None:
            stack.append(x.right)
        if x.left is not None:
            stack.append(x.left)
        print(x.val,end=" ")
    print()

def height(root):
    if root is None:
        return 0
    '''
    if root.left is None and root.right is None:
        return 1
    '''
    return (max( height(root.left),height(root.right)) + 1)

def findMin(root):
    if root is None:
        return 
    curr = root
    while(curr.left != None):
        curr = curr.left
    return curr.val

def findMax(root):
    if root is None:
        return
    curr = root
    while(curr.right != None):
        curr = curr.right
    return curr.val
def LCA(root,p,q):
    if root is None:
        return None
    curr = root
    while(curr):
        if p < curr.val and q < curr.val:
            curr = curr.left
        elif p > curr.val and q > curr.val:
            curr = curr.right
        else:
            break
    return curr.val

def mirror(root):
    if root is None:
        return None
    mirror(root.left)
    mirror(root.right)
    root.left , root.right = root.right, root.left

def inorderSuccessor( root, x):
        # Code here
        if root is None:
            return -1
        curr = root 
        stack = []
        prev = -9999
        while(stack or curr):
            if(curr):
               stack.append(curr)
               curr = curr.left
            else:
                curr = stack.pop()
                if prev == x:
                    return curr.val
                prev = curr.val
                curr = curr.right

def PathSum(root,maxSum,curSum):
    if root is None:
        return
    
    curSum = curSum +root.val
    if (root.left == None and root.right == None): 
        if curSum > maxSum:
            maxSum = curSum
            
    if root.left is not None:
        maxSum = PathSum(root.left,maxSum,curSum)
    if root.right is not None:
        maxSum = PathSum(root.right,maxSum,curSum)
    return maxSum


root = None
root = insertItr(root, 2)
insertItr(root,1)
insertItr(root, 3)


'''
root = insertItr(root, 20)
insertItr(root,30)
insertItr(root, 32)
insertItr(root, 21)
insertItr(root, 17)
insertItr(root, 16)
insertItr(root, 15)
insertItr(root, 11)
insertItr(root, 18)
insertItr(root, 9)
#inorder(root)
#preorderItr(root)
#levelOrder(root)
#print("Height ",height(root))
#print("Min ",findMin(root))
#print("Max ",findMax(root))
#print("LCA ",LCA(root,21,18))
#mirror(root)
'''
levelOrder(root)

print("Height ",height(root))

print("Inorder successor ",inorderSuccessor(root,15))
print(PathSum(root,-999,0))