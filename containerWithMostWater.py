arr = [1,8,6,2,5,4,8,3,7]

a_pointer = 0
b_pointer = len(arr)-1
maxArea = -9089765
area = 0
while a_pointer < b_pointer:
    if arr[a_pointer] > arr[b_pointer]:
        area = (b_pointer - a_pointer) * arr[b_pointer]
        maxArea = max(maxArea,area)
        b_pointer -= 1
    else:
        area = (a_pointer - b_pointer) * arr[a_pointer]
        maxArea = max(maxArea,area)
        a_pointer += 1
print(maxArea)