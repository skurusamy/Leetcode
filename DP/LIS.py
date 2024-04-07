def LIS(arr1,arr2,m):
    dp = [[-1 for i in range(m+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(m+1):
            if i ==0  or j == 0:
                dp[i][j] = 0
    
    for i in range(1,m+1):
        for j in range(1,m+1):
            if arr1[i-1] == arr2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp)
    return dp[m][m]        

arr = [10,22,9,33,21,50,41,60]
arr1 = sorted(arr)
print(arr1)
print(LIS(arr,arr1,len(arr)))