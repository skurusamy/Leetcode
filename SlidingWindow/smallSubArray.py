#smallest sub array with greater sum 
import sys
arr = [2, 1, 5, 2, 3, 2]
s=7 
start = 0
arr_sum = 0
length = sys.maxsize
for end in range(len(arr)):
    arr_sum += arr[end]
    while arr_sum >= s:
        length = min(length, end - start +1)
        arr_sum -= arr[start]
        start += 1
if length == sys.maxsize:
    print("0")
print(length)

