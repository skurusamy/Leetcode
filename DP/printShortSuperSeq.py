def printShortSuperSeq(x,y,n, m):
    ans = []
    dp = [[-1 for i in range(m+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j ==0:
                dp[i][j] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
                ans.append(x[i-1])
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if dp[i-1][j] > dp[i][j-1]:
                    ans.append(x[i-1])
                else:
                    ans.append(y[j-1])
    return ans
x = "abcdef"
y = "abrdfy"
print(printShortSuperSeq(x,y,6,6))
