'''
find union and intersection of two sorted arrays
'''

arr1 = [1,2,3,4,4,5,6]
arr2 = [1,2,4,5,7]
intersection =set()
union = set()
if len(arr1) < len(arr2):
    min_array = arr1
    big_array = arr2
else:
    min_array = arr2
    big_array = arr1
for i in min_array:
    if i in big_array:
        intersection.add(i)
for i in arr1:
    union.add(i)
for j in arr2:
    union.add(j)
print(union)
print(intersection)
