from gettext import find


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

def findMax(root):
    if root is None:
        return
    while root.right is not None:
        root = root.right
    return root.val

def LevelOrder(root):
    levelOrder = []
    if root is None:
        return None
    queue = [root,]
    while(queue):
        for i in range(len(queue)):
            curr = queue.pop(0)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
            levelOrder.append(curr.val)
        levelOrder.append(" ")
    print("Level Order: ",levelOrder)


def leftRightView(root):
    rightView = []
    leftView =[]
    if root is None:
        return None
    queue = [root,]
    while(queue):
        size  = len(queue)
        for i in range(size):
            curr = queue.pop(0)
            if i == 0:
                leftView.append(curr.val)
            if i == size -1:
                rightView.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    print("LeftView: ",leftView)
    print("RightView: ",rightView)

def height(root):
    if not root:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)

    return max(lheight, rheight) +1

def findPathHelper(root,currPath,allPaths):
    if root is None:
        return
    currPath.append(root.val)
    if root.left is None and root.right is None:
        allPaths.append(list(currPath))
    findPathHelper(root.left, currPath,allPaths)
    findPathHelper(root.right,currPath,allPaths)

    del currPath[-1]

def findAllPaths(root):
    if not root:
        return
    allPaths = []
    findPathHelper(root,[],allPaths)
    return allPaths

def pathSum(root,sum):

    if root is None:
        return False
    if root.val == sum  and root.left is None and root.right is None :
        return True
    return pathSum(root.left, sum - root.val) or pathSum(root.right, sum - root.val)



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

LevelOrder(root)
leftRightView(root)
print("Height: ",height(root))

print("All Paths: ",findAllPaths(root))
print("SumPath ",pathSum(root,143))
