from typing import ChainMap


class Heap:
    def __init__(self):
        self.heap =[]
        self.capacity = -1

    def heapifyUp(self):
        if self.capacity == -1:
            return
        index = self.capacity
        parentIndex = (index)//2
        while self.heap[parentIndex] > self.heap[index] and index > 0: 
            self.heap[parentIndex] , self.heap[index] = self.heap[index] , self.heap[parentIndex] 
            index = parentIndex
            parentIndex = (index)//2

    def heapifyDown(self):
        if self.capacity == -1:
            return
        smallIndex = 0
        index =0
        flag = 1
        while index <= self.capacity and flag == 1:
            flag =0
            leftChild = (2*index) + 1
            rightChild = (2*index) +2
            if leftChild <= self.capacity and self.heap[leftChild] < self.heap[smallIndex]:
                smallIndex = leftChild
                flag =1
            if rightChild <=self.capacity and self.heap[rightChild] < self.heap[smallIndex]:
                smallIndex = rightChild
                flag = 1
            self.heap[index],self.heap[smallIndex] = self.heap[smallIndex],self.heap[index]
            index = smallIndex
            


    def push(self,ele):
        self.heap.append(ele)
        self.capacity += 1
        self.heapifyUp()
    
    def pop(self):
        self.heap[0],self.heap[self.capacity] = self.heap[self.capacity],self.heap[0]
        x = self.heap.pop()
        self.capacity -= 1
        self.heapifyDown()
        

h = Heap()
h.push(10)
h.push(20)
h.push(1)
h.push(3)
print(h.heap)
h.pop()
print(h.heap)