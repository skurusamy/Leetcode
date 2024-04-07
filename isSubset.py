arr2 = [1,4,5,6,0]
arr1 = [1,12,5,8,9]
i=0
j=0
arr1.sort()
arr2.sort()
flag1 = True
flag2 = True
print(arr1)
print(arr2)
while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
        i += 1
        j += 1

    elif arr2[j] < arr1[i]:
        j += 1
        flag2 = False
    elif arr1[i] < arr2[j]:
         i +=1
         flag1 = False

if flag1 == False and flag2 == False:
    print("False")
elif flag2 == True and  j == len(arr2):
    print("array2 is subset of array1")
elif flag1 == True and i == len(arr1):
    print("Array1 is subset of array2")

