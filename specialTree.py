class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def toTree(pre, preL, index_ptr, n):
    index = index_ptr[0]
    if index == n:
        return
    temp = node(pre[index])
    index_ptr[0]  += 1
    if preL[index] == 'N':
            temp.left = toTree(pre, preL, index_ptr, n)
            temp.right = toTree(pre, preL, index_ptr, n)
    return temp


def inOrder(root):
    if root is None:
        return
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif (stack):
            current = stack.pop()
            print(current.val)
            current = current.right
        else:
            break

def preOrder(root):
    if root is None:
        return
    print(root.val,end=" ")
    preOrder(root.left)
    preOrder(root.right)
def preOrderItr(root):
    if root is None:
        return
    current = root
    stack = []
    stack.append(root)
    while len(stack)>0:

        current = stack.pop()
        print(current.val,end=" ")
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

pre = [10, 30, 20, 5, 15]
preL = ['N', 'N', 'L', 'L', 'L']
index = [0]
root = toTree(pre, preL, index, len(pre))
inOrder(root)
preOrder(root)
print()
preOrderItr(root)
