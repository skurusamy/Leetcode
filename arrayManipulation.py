'''

Sample Input
5 3
1 2 100
2 5 100
3 4 100
Sample Output
200
Explanation
After the first update the list is 100 100 0 0 0.
After the second update list is 100 200 100 100 100.
After the third update list is 100 200 200 200 100.
The maximum value is 200.

'''

# enter number of rows in result

res_col = int(input("Enter the number of columns in result array: "))
arr_row = int(input("Enter array rows: "))
arr = []
ans = [0]*res_col
max1 = -99999;
print("Enter array elements: ")
for i in range(arr_row):
    col =[]
    for j in range(3):
        col.append(int(input()))
    arr.append(col)

for i in range(arr_row):
    a = arr[i][0]
    b = arr[i][1]
    k = arr[i][2]
    for j in range(res_col):
        if j >= a-1 and j <= b-1:
            ans[j] = ans[j] + k

    if max1 < max(ans):
        max1 = max(ans)
    print(ans)
print(max1)