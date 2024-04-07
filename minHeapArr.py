class MinHeap:
    def __init__(self,size):
        self.minheap = [0]*size
        self.capacity = size
        self.cur_size = 0

    def bubbleup(self,eleIndex):
        parentIndex = (eleIndex-1) // 2
        while eleIndex > 0 and self.minheap[eleIndex] < self.minheap[parentIndex]:
            x = self.minheap[eleIndex]
            self.minheap[eleIndex]= self.minheap[parentIndex]
            self.minheap[parentIndex] = x
            eleIndex = parentIndex
            parentIndex = (eleIndex-1) //2

    def bubbleDown(self,parentIndex):
        smallIndex = parentIndex
        leftIndex = (parentIndex * 2) + 1
        rightIndex = (parentIndex * 2) + 2
        if leftIndex < self.cur_size and self.minheap[parentIndex] > self.minheap[leftIndex]:
            smallIndex = leftIndex
        if rightIndex < self.cur_size and self.minheap[parentIndex] > self.minheap[rightIndex]:
            smallIndex = rightIndex
        if smallIndex != parentIndex:
            x = self.minheap[smallIndex]
            self.minheap[smallIndex] = self.minheap[parentIndex]
            self.minheap[parentIndex] = x
            self.bubbleDown(smallIndex)



    def insert(self,ele):
        #array is full
        if self.cur_size == self.capacity:
            return False
        else:
            self.minheap[self.cur_size] = ele
            self.bubbleup(self.cur_size)
            self.cur_size += 1
            return True
    def delete(self,ele):
        #No elements in the array
        if self.cur_size == 0:
            return False
        else:
            eleIndex = self.minheap.index(ele)
            self.cur_size -= 1
            self.minheap[eleIndex] = self.minheap[self.cur_size]
            self.minheap[self.cur_size]=0
            self.bubbleDown(eleIndex)

            return True
    def print(self):
        for i in self.minheap:
            print(i,end=" ")

h =MinHeap(7)
h.insert(20)
h.insert(19)
h.insert(18)
h.insert(17)
h.insert(16)
h.insert(15)
h.insert(10)
h.delete(10)
h.delete(15)
h.print()