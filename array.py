class Array:
    def __init__(self,arr):
        self.arr = arr
    def getEle(self,index):
        return self.arr[index]
    def push(self,element):
        self.arr.append(element)
    def pop(self):
        ans = self.arr[len(self.arr)-1]
        self.arr.remove(ans)
        return ans
    def printArr(self):
        print(self.arr)
    def delete(self,index):
        for i in range(index, len(self.arr)-1):
            self.arr[index] = self.arr[index+1]
            index += 1
        self.arr.remove(self.arr[len(arr)-1])
# main 

arr = [1,2,3,4,5]
array = Array(arr)
print(array.getEle(4))
#print(array.pop())
array.delete(2)
array.printArr()
