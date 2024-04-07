''''

Sample Input 1
3
3 2 1
Sample Output 1
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3

'''

n = int(input("Enter n: "))
arr = []
count =0
for i in range(n):
    arr.append(int(input()))
for i in range(len(arr)-1):
    for j in range(i,len(arr),1):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            count += 1
    print(arr)
print(count)