class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.min = 0
    def push(self,val):
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min = val
            return
        if val < self.min:
            newVal = (2 * val ) - self.min
            self.min = val
            self.stack.append(newVal)
            return 
        self.stack.append(val)
    def pop(self):
        if len(self.stack) == 0:
            print("No  elements")
            return
        x = self.stack.pop()
        if x < self.min:
            self.min = originalVal =  2*self.min - x
            print("pop:",originalVal)

    def getMin(self):
        print("min:",self.min)


s = Stack()
s.push(10)
s.push(8)
s.push(6)
s.push(12)
s.getMin()
s.pop()
s.pop()
s.getMin()
print(s.stack)
