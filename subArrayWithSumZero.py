'''
arr[] = {1, 4, -2, -2, 5, -4, 3}

If we consider all prefix sums, we can
notice that there is a subarray with 0
sum when :
1) Either a prefix sum repeats or
2) Or prefix sum becomes 0.

Prefix sums for above array are:
1, 5, 3, 1, 6, 2, 5

Since prefix sum 1 repeats, we have a subarray
with 0 sum. 
'''
#arr = [1, 4, -2, -2, 5, -4, 3]
arr = [0,0,1]
sum =0
sumArray = []
flag = -1
for i in range(1,len(arr)):
    sum = sum + arr[i]
    if sum not in sumArray:
        sumArray.append(sum)
    if sum in sumArray or sum == 0:
        flag = 0
if flag == 0:
    print("YES")
else:
    print("NO")    
