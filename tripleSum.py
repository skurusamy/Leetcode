'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
'''
def findSum(arr, target,a_pointer):
    b_pointer = len(arr)-1
    while a_pointer <= b_pointer:
        if arr[a_pointer]+ arr[b_pointer] == target:
            return [arr[a_pointer],arr[b_pointer], -(arr[a_pointer]+ arr[b_pointer])]
        elif arr[a_pointer]+ arr[b_pointer] < target:
            a_pointer += 1
        else:
            b_pointer -= 1
def tripletSum(arr):
    arr.sort()
    res = []
    for i in range(len(arr)):
        ans = findSum(arr,-arr[i],i+1)
        if ans:
            res.append(ans)
    return res

arr = [-3, 0, 1, 2, -1, 1, -2]
print(tripletSum(arr))