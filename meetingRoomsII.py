import heapq
intervals = [[0,30],[5,10],[15,20]]
rooms = 1
minHeap = []
intervals = sorted(intervals, key= lambda x:x[0])
print(intervals)
heapq.heapify(minHeap)
heapq.heappush(minHeap,intervals[0][1])
for i in range(1,len(intervals)):
    end = minHeap[0]
    if intervals[i][0] < end:
        heapq.heappop(minHeap)
        rooms += 1
    heapq.heappush(minHeap,intervals[i][1])
print(len(minHeap))