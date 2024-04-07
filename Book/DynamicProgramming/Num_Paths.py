'''
Given 2d array Find path from top left to bottom right. 
Only can move down and right.
there'll be some offlimits

'''
def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j],end=" ")
        print()
def path(arr):
    ans = [[0 for i in range(len(arr[0])) ] for j in range(len(arr))]
    for i in range(len(arr)):
        if arr[i][0] != 0:
            ans[i][0] = 1  
    for i in range(len(arr[0])):
        if arr[0][i] != 0:
            ans[0][i] = 1
    for i in range(1,len(arr)):
        for j in range(1,len(arr[0])):
            if arr[i][j] != 0:
                ans[i][j] = ans[i-1][j] + ans[i][j-1]
    print("ans")
    display(ans)
arr = [[1,1,1,0],[0,0,1,1],[1,1,1,1],[0,1,1,1]]
print("original")
display(arr)
path(arr)