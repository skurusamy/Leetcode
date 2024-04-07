'''
move all the negative elements to one side
Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
'''
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
i =0;
j = len(arr)-1
while(i<j):
    if arr[i] < 0:
        i += 1
    if arr[j] > 0:
        j -= 1
    if arr[i] > 0 and arr[j] < 0  and i<j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
print(arr)