'''

Print the largest (maximum) hourglass sum found in .
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output
19

'''

arr =[]
sum = []
print("Enter array: ")
for i in range(6):
    col=[]
    for j in range(6):
        col.append(int(input()))
    arr.append(col)
for i in range(4):
    for j in range(4):
        sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
print(sum)
print(max(sum))
