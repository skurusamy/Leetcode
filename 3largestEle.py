'''
Given an array with all distinct elements, find the largest three elements. Expected time complexity is O(n) and extra space is O(1). 
Examples :

Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23
'''
import sys
max1 = max2 = max3 = -sys.maxsize
arr = [10, 4, 3, 50, 23, 90]
for i in arr:
    if i > max1:
        max3 = max2
        max2 = max1
        max1 = i
    elif i > max2:
        max3 = max2
        max2 = i
    elif i > max3:
        max3 = i 

print(max1,max2,max3)
