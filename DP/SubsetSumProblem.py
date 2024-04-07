''''
Varient of KnapSack Problem

If the subset present so that the sum is equal to 11
'''


arr = [2,3,7,8,10]
sum = 10
n = len(arr)
dp = [[False for i in range(sum +1)] for j in range(n+1)]

for i in range(n+1):
    for j in range(sum+1):
        if j == 0:
            dp[i][j] = True
#print(dp)
for i in range(1, n+1): # i is n
    for j in range(1,sum+1): # j is sum
        if arr[i-1] <= j:
            dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][sum])