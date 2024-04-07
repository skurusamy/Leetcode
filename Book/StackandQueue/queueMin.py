class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enque(self,val):
        self.queue.append(val)
    def getMin(self):
        print("Min:", self.min)
    def deque(self): # loop over the queue to find min
        min = 999999
        index = 9999
        for i in range(len(self.queue)):
            if self.queue[i] < min:
                min = self.queue[i]
                index = i
        print(self.queue.pop(index))




q = Queue()
q.enque(10)
q.enque(1)
q.enque(6)
q.enque(12)
q.deque()
q.deque()
print(q.queue)