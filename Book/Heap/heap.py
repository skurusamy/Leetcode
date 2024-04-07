import heapq
def createminHeap(heap):
    heapq.heapify(heap)
    ip = [21,23,15,2,1,45,12,10]
    for i in ip:
        heapq.heappush(heap,i)


def createmaxHeap(heap):
    heapq.heapify(heap)
    ip = [21,23,15,2,1,45,12,10]
    for i in ip:
        val = (-1 * i)
        heapq.heappush(heap,val)  
  
def kSmallest(heap,k):
    count = 1
    while count <= k:
        x = heapq.heappop(heap)
        count += 1
    return x

def kLargest(heap,k):
    count = 1
    while count <= k:
        x = heapq.heappop(heap)
        count += 1
    return -x
'''
minheap = []
createminHeap(minheap)
print("Min:",minheap)
k =3
print(kSmallest(minheap,k))
'''
maxheap = []
k =3
createmaxHeap(maxheap)
print(maxheap)
print("Max",kLargest(maxheap,k))


