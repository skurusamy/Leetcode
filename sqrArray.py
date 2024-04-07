'''
Given a sorted array, 
create a new array containing squares of all the numbers of the input array in the sorted order.
'''
import math
def squaredArr(arr):
    sqr = []
    a_pointer = 0
    b_pointer = len(arr) -1 
    while a_pointer <= b_pointer:
        if abs(arr[a_pointer]) < abs(arr[b_pointer]):
            val = arr[b_pointer] * arr[b_pointer]
            b_pointer -= 1
        else:
            val = arr[a_pointer] * arr[a_pointer]
            a_pointer += 1
        sqr.insert(0,val)
    return sqr
arr= [-2, -1, 0, 2, 3]
print(squaredArr(arr))