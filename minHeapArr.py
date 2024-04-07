class minHeap:
    def __init__(self,size) -> None:
        self.size = size
        self.arr = [-1] * (size)
        self.cursize = -1

    def heapifyUp(self, curIndex):
        if curIndex <=0 :
            return
        parentIndex = (curIndex - 1)// 2
        while parentIndex >= 0 and self.arr[parentIndex] > self.arr[curIndex]:
            self.arr[parentIndex], self.arr[curIndex] = self.arr[curIndex],self.arr[parentIndex]
            curIndex = parentIndex
            parentIndex = (curIndex - 1)// 2

    def insert(self,ele):
        self.cursize += 1
        self.arr[self.cursize] = ele
        self.heapifyUp(self.cursize)
        

    def heapifyDown(self,curIndex):
        if curIndex > self.cursize:
            return 
        leftChild = (2*curIndex) + 1
        rightChild = (2*curIndex) + 2
        smallIndex = curIndex
        
        if leftChild <= self.cursize and self.arr[leftChild] < self.arr[curIndex]:
                smallIndex = leftChild
        if rightChild <= self.cursize and self.arr[rightChild] < self.arr[curIndex]:
                smallIndex = rightChild
        if smallIndex != curIndex:
                self.arr[smallIndex], self.arr[curIndex] = self.arr[curIndex], self.arr[smallIndex]
                self.heapifyDown(smallIndex)
       
            

    def delete(self,ele):
        curIndex = self.arr.index(ele)
        self.arr[self.cursize], self.arr[curIndex] = self.arr[curIndex],self.arr[self.cursize]
        self.arr[self.cursize] = -1
        self.cursize -= 1
        self.heapifyDown(curIndex)
        

heap = minHeap(10)
heap.insert(8)
heap.insert(5)
heap.insert(6)
heap.insert(4)
heap.insert(2)
print(heap.arr)
heap.delete(2)
print(heap.arr)