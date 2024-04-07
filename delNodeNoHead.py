class node:
    def __init__(self, val):
        self.val = val
        self.next = None
def printNode(start):
    if start == None:
        return
    curr = start
    while(curr!=None):
        print(curr.val)
        curr = curr.next
    return
def delete(ele):
    if ele is None:
        return
    if ele.next is None:
        print("lastNode")
        return
    curr = ele.next
    if(ele.next!=None):
        ele.val = (curr).val
        ele.next = curr.next
    return


node1 = node(5)
node2 = node(10)
node3 = node(98)
node4 = node(34)
node5 = node(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
printNode(node1)
delete(node2)
print("******")
printNode(node1)
