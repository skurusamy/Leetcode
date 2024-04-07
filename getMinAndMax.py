'''
get the minimum and maximum element in an array

'''
import sys
arr = [12,15,2,6,8,122,90]
min_ele = sys.maxsize
max_ele = -sys.maxsize
for i in arr:
    if i > max_ele:
        max_ele = i
    if i < min_ele:
        min_ele = i
print(max_ele,min_ele)