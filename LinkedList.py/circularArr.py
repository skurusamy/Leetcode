def findIdx(arr,ele):
    idx = arr.index(ele)
    idx += (ele)% len(arr)
    return idx


def isCycle(arr):
    slow = 0
    fast = 0
    while slow != fast:
        slow = findIdx(arr[slow])
        fast = findIdx(findIdx(arr[fast]))
    


arr = [1, 2, -1, 2, 2]
print(isCycle(arr))