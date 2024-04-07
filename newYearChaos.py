''''
2 1 5 3 4   q = [2, 1, 5, 3, 4]
3
'''
n = int(input("Enter the elements in the array: "))
arr = []
flag = 0
overall = 0
for i in range(n):
    arr.append(int(input()))
'''
using bubble sort


temp =[0]*len(arr)
for i in range(len(arr)-1):
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            a = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = a
            temp[arr[j+1]-1] = temp[arr[j+1]-1] + 1
    print(arr, temp)
for i in temp:
    if i <= 2:
        overall += i
    else:
        overall = 0
        break;
if overall == 0 :
    print("Not possible")
else:
    print(overall)
'''
## to reduce time complexity

first = 1
second = 2
third = 3
for i in arr:
    if i == first:
        first = second
        second = third
        third += 1
        flag = 0
    elif i == second:
        overall += 1
        second = third
        third += 1
        flag = 0
    elif i == third:
        overall += 2
        third += 1
        flag = 0
    else:
        flag = 1
        break;
if flag == 0:
    print(overall)
else:
    print('Too chaotic')