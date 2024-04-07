import heapq
def furthestBuilding(heights, bricks, ladder):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        maxHeap = []
        heapq.heapify(maxHeap)
        for i in range(1,len(heights)):
            if heights[i -1] > heights[i]: 
                continue
            if heights[i-1] < heights[i]:
                diff = heights[i] - heights[i-1]
                if len(maxHeap) < ladder:
                    heapq.heappush(maxHeap,diff)
                else:
                    br = diff
                    if len(maxHeap) > 0 and  maxHeap[0]< diff:
                        br = heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap,diff)
                    if bricks-br >= 0:
                            bricks -= br
                    else:
                            return i -1
        return len(heights) -1
print(furthestBuilding([4,12,2,7,3,18,20,3,19]
,10
,2))