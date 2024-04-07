import  heapq
def kthSmallest( matrix, k):
        nums =[]
        heapq.heapify(nums)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(nums, matrix[i][j])
        print(nums)
        i = 0
        while(i<k-1):
            heapq.heappop(nums)
            i += 1
        return heapq.heappop(nums)

print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))