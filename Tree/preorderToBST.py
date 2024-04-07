class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    if len(preOrderTraversalValues) == 0:
        return None
    currentVal = preOrderTraversalValues[0]
    rightIdx = len(preOrderTraversalValues) 
    for i in range(1,len(preOrderTraversalValues)):
        if currentVal <= preOrderTraversalValues[i]:
            rightIdx = i
            break
		
    leftTree = reconstructBst(preOrderTraversalValues[1:rightIdx])
    rightTree = reconstructBst(preOrderTraversalValues[rightIdx:])
    return BST(currentVal,leftTree,rightTree)

reconstructBst([10, 4, 2, 1, 5, 17, 19, 18])