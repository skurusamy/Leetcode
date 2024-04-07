'''
Rearrange array in alternating positive & negative items with O(1) extra space
Given an array of positive and negative numbers, arrange them in an alternate fashion such that 
every positive number is followed by negative and vice-versa maintaining the order of appearance. 
Number of positive and negative numbers need not be equal. 
If there are more positive numbers they appear at the end of the array. If there are more negative numbers, 
they too appear in the end of the array.

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Idea:
Move all the negative to one end
Rearrange the elements 
'''
def swap(x,y):
    return y,x

def moveNegativetoRight(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] >= 0:
            left +=1
        if arr[right] < 0:
            right -= 1
        if arr[left] < 0 and arr[right] >= 0:
            arr[left],arr[right] = swap(arr[left],arr[right])
            left += 1
            right -= 1
    return arr
def changePositions(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] >= 0 and  left %2 !=0:
            left += 1
        if arr[left] >= 0 and arr[right] < 0 and left%2==0:
            arr[left],arr[right] =  swap(arr[left],arr[right])
            left += 1
            right -= 1
    return arr

#main
#arr = [1, 2, 3, -4, -1, 4]
arr =[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
arr = moveNegativetoRight(arr)
print(arr)
arr = changePositions(arr)
print(arr)