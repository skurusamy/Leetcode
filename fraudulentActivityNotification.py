'''
Sample Input 0
9 5
2 3 4 2 3 6 8 4 5
Sample Output 0
2
Input
5 3
10 20 30 40 50
ans : 1

'''
'''
import math
n = int(input("Enter number of elements in an array: "))
d = int(input("Enter lookback days for median: "))
arr = []
notification = 0
print("Enter array elements: ")
for i in range(n):
    arr.append(int(input()))
j = 0
for i in range(d,n,1):
    temparr = arr[j:d]
    temparr.sort()
    if d % 2 != 0:
        median = int(math.floor((0 + d - 1) / 2))
        com = temparr[median]
    else:
        com = (temparr[d // 2] + temparr[(d - 1) // 2]) / 2
    if arr[d] >= 2 * com:
        notification  += 1
    d += 1
    j += 1
print(notification)
'''


