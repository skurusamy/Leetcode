'''
Check if key is present in every segment of an array
arr[] = { 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3} 
x = 3 
k = 3 
Output : Yes 
There are 4 non-overlapping segments of size k in the array, {3, 5, 2}, {4, 9, 3}, {1, 7, 3} and {11, 12, 3}. 3 is present all segments.
Input : 
arr[] = { 21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25} 
x = 23 
k = 5 
Output :Yes 
Input :arr[] = { 5, 8, 7, 12, 14, 3, 9} 
x = 8 
k = 2 
Output : No
'''
arr = [ 5, 8, 7, 12, 14, 3, 9]
key = 8
k = 2
flag = 0
for i in range(len(arr)):
    if i % k ==0:
        subArray  = arr[i:i+k]
        print(subArray)
        if key not in subArray:
            flag = 1
if flag == 1:
    print("No")
else:
    print("YES")