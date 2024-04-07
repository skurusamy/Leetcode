def twoSum(arr,target):
    prevMap = {}
    for i in range(len(arr)):
        sec_val = target - arr[i]
        if sec_val in prevMap.keys():
            return [prevMap[sec_val],i]
        if arr[i] not in prevMap:
            prevMap[arr[i]] = i
    return []


arr = [1,2,1,3,5]
target = 2
print(twoSum(arr,target))