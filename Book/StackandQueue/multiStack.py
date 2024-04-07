'''
Stack  object
===========
Stack list
current pointer

Nstack 
top of stack = // current position of a list
stackComplete = all the elements in individual stack
index = 
nextAvailable -> next index that is available

'''
class StackPool:
    def __init__(self) -> None:
        self.stackPool = []
        self.stackPoolIndex = 0
        self.stacktop = [-1,-1,-1]
        self.previousAvailable = []
        
    def push(self,stackNo,value):
        self.stackPool.append(value)
        if self.stacktop[stackNo] == 0:
            self.previousAvailable.append(-1)
        else:
            self.previousAvailable.append(self.stacktop[stackNo])
        self.stacktop[stackNo] = self.stackPoolIndex
        self.stackPoolIndex += 1
        
    def display(self):
        print(self.stackPool)

    def pop(self,stackNum):
        pos = self.stacktop[stackNum]
        prev = self.previousAvailable[pos]
        x = self.stackPool.pop(pos)
        self.stacktop[stackNum] = prev

s = StackPool()
s.push(0,11)
s.push(0,19)
s.push(1,10)
s.push(2,12)
s.push(2,100)
s.push(0,20)
s.pop(0)
s.display()


