import heapq
arr =[1,5,6,2,4,7,8] #easiest way is to sort and return len-k th element but takes more complexity 
#use min heap
k=4
index = 0
minHeap = []
'''
heapq.heapify(minHeap)
for i in arr:
    heapq.heappush(minHeap,i)
    print(minHeap)
    #largest k element
    if len(minHeap) > k:
        heapq.heappop(minHeap)
print(heapq.heappop(minHeap))
'''
# k smallest 
heapq.heapify(minHeap)
for i in arr:
    heapq.heappush(minHeap,i)
print(minHeap)
index =1
while index < k:
    heapq.heappop(minHeap)
    index += 1
print(heapq.heappop(minHeap))