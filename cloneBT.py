class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

l = [6, 3, 'L', 6, 8, 'R', 3, 1, 'L', 3, 5, 'R', 1, 3, 'X', 5, 6, 'X']
for i in range(0,len(l),3):
    print(l[i])