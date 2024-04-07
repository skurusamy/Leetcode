'''
ar1[] = {1, 5, 10, 20, 40, 80} 
ar2[] = {6, 7, 20, 80, 100} 
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
Output: 20, 80
'''
arr1= [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
i = j = k = 0
output = set()
while i < len(arr1) and j < len(arr2) and k < len(arr3):
    if arr1[i] == arr2[j] == arr3[k]:
        output.add(arr1[i])
        i +=1
        j +=1
        k +=1
    elif arr1[i] < arr2[j]:
        i += 1
    elif arr2[j] < arr3[k]:
        j += 1
    else:
        k += 1
print(output)    
    