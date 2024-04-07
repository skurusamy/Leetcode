'''
You are given a list of n-1 integers and these integers are in the range of 1 to n. 
There are no duplicates in the list.
One of the integers is missing in the list. Write an efficient code to find the missing integer.
'''
import sys
def missingEle(arr):
    max_ele =-sys.maxsize
    for i in arr:
        if i > max_ele:
            max_ele = i
        dic[i] = True
    for i in range(1,max_ele+1):
        if i  not in dic:
            return i;
'''
other method
Find sum of n numbers using ((n+1)*(n+2))/2 
and subtract each element from array
'''
def alternateMethod(arr):
    n = len(arr)
    # n = sizeof(arr)/sizeof(arr[0])
    sum =  ((n+2)*(n+1)) / 2
    for i in arr:
        sum = sum - i
    return sum



arr = [1, 2, 4, 6, 3, 7, 8]
dic = {}
print(missingEle(arr))
print("alternate Method:",alternateMethod(arr))


