def twoSum(arr,target):
    a_pointer = 0
    b_pointer = len(arr) -1
    while a_pointer < b_pointer:
        if arr[a_pointer] + arr[b_pointer]  == target:
            return a_pointer,b_pointer
        if arr[a_pointer] + arr[b_pointer] >= target:
            b_pointer -= 1
        else:
            a_pointer += 1
    return -1,-1


arr = [2, 5, 9, 11]
target = 12
print(twoSum(arr,target))