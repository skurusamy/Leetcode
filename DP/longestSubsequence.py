def longestSubSequence(x,y,n, m):
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
                dp[i][j] =  max(dp[i-1][j],dp[i][j-1])
    return ans

def longestSubSequenceAlt(x,y,n, m):
    ans=[]
    if n ==0 or m == 0:
        return 0
    i = 0 
    index = 0
    while (i < n):
        j = index
        while j < m:
            if x[i] == y[j]:
                ans.append(x[i])
                index = j
                break
            else:
                j += 1
        i += 1
    return ans

x= "ZXVVYZW"
y= "XKYKZPW"
m = len(x)
n = len(y)
print(longestSubSequence(x,y,m,n))
