class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def levelOrder(root):
    if root is None:
        return
    q=[]
    q.append(root)
    while len(q)>0:
        print(q[0].val, end=" ")
        curr = q.pop(0)
        if curr.left != None:
            q.append(curr.left)
        if curr.right != None:
            q.append(curr.right)
def swap(n1,n2):
    temp = n1
    n1= n2
    n2 = temp
    return n1,n2

def Mirror(root):
    if root is None:
        return
    if root.left!=None or root.right!=None:
        #root.left,root.right=swap(root.left,root.right)
        root.left, root.right =(root.right, root.left)
    if root.left !=None:
        Mirror(root.left)
    if root.right != None:
        Mirror(root.right)
def nullLevelOrder(root):
    if root is None:
        return
    q =[]
    q.append(root)
    level_count=0
    node_level = {}
    while q:
        node_count = 0
        count = len(q)
        while count>0:
            node = q.pop(0)
            if node is None:
                print("Null", end=" ")
            else:
                q.append(node.left)
                q.append(node.right)
                print(node.val,end=" ")
                node_count += 1
            count -=1
        node_level[level_count] = node_count
        level_count += 1
        print()
    return node_level

def copyLR(root,dic):
    if root is None:
        return
    newNode = node(root.val)
    dic[newNode] = root
    newNode.left = copyLR(root.left,dic)
    newNode.right = copyLR(root.right,dic)
    return newNode
def cloneTree(root):
    if root is None:
        return
    dic ={}
    ans =copyLR(root,dic)
    return ans
def diagonalSum(root,vd,diagonal_sum):
    if root is None:
        return
    if vd not in diagonal_sum:
        diagonal_sum[vd]=0
    diagonal_sum[vd] += root.val
    diagonalSum(root.left,vd+1,diagonal_sum)
    diagonalSum(root.right,vd,diagonal_sum)

def removeHalfNode(root):
    if root is None:
        return
    root.left = removeHalfNode(root.left)
    root.right = removeHalfNode(root.right)
    if root.right is None and root.left is None:
        return root
    if root.left != None and root.right == None:
        newRoot = root.left
        temp = root
        root = None
        del(temp)
        return newRoot
    if root.left == None and root.right != None:
        newRoot = root.right
        temp = root
        root = None
        del (temp)
        return newRoot
    return root

def getLeaves(root,ans):
    if root is None:
        return
    if root.right is None and root.left is None:
        ans.append(root.val)
    getLeaves(root.left,ans)
    getLeaves(root.right,ans)

def minDepth(root):
    if root is None:
        return
    q = []
    q.append(root)
    levelCount = 0
    while(q):
        count = len(q)
        while count > 0:
            node = q.pop(0)
            if node is None:
                return levelCount
            else:
                q.append(node.left)
                q.append(node.right)
                count -= 1
        levelCount +=1
    return levelCount
def getHeight(root):
    if root is None:
        return 0
    h = getHeight(root.left)
    n = getHeight(root.right)
    if h > n: # h <n return 1+h # minDepth
        return 1 + h
    else:
        return 1+n
def hasSumPath(root,sum):
    if root is None:
        return False
    if root.left == None and root.right == None and sum - root.val ==0:
        return  True
    else:
        return hasSumPath(root.left,sum - root.val) or hasSumPath(root.right,sum - root.val)
def lca(root,p,q):
    if root is None:
        return
    if root.val == p or root.val == q:
        return root
    lval = lca(root.left,p,q)
    rval = lca(root.right,p,q)
    if lval and rval:
        return root
    if lval:
        return lval
    else:
        return rval


node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
node6 = node(6)
node7 = node(7)
root = node1
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node6
node4.right=node5
node5.left = node7
node_level={}

#node_level = nullLevelOrder(root)
#print(getHeight(root))
#root = node1
nullLevelOrder(root)
print("********")
Mirror(root)
nullLevelOrder(root)
'''
#clone tree

cloneNode = cloneTree(root)
nullLevelOrder(cloneNode)

#diagonal_sum
diagonal_sum ={}
diagonalSum(root,0,diagonal_sum)
print(diagonal_sum)
# even odd difference
odd =0
even =0
for i in node_level:
    if i % 2 == 0 :
        even += node_level[i]
    else:
        odd += node_level[i]
print(odd-even)
li = list(node_level.keys())
print(li)
print(li.index(max(node_level.values())))
#delete node with one child
print("**********")
newRoot= removeHalfNode(root)
nullLevelOrder(newRoot)
ans=[]
getLeaves(root,ans)
print(ans)

print(node_level)
print(minDepth(root))
'''
#nullLevelOrder(root)
#print(hasSumPath(root,11))
#print(lca(root,2,3).val)
