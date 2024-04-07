'''
Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; after removing the duplicates in-place return the length of the 
subarray that has no duplicate in it.
'''

def removeDuplicate(arr):
  pointer = 1
  i = 0
  while i < len(arr):
    if arr[pointer-1] != arr[i]:
      arr[pointer] = arr[i]
      pointer += 1
    i+= 1
  return pointer

arr = [2, 3, 3, 3, 6, 9, 9]
print(removeDuplicate(arr))