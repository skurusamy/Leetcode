'''
Factorial of a large number
using dynamic programming
'''

#main
import sys
def factorial(n):
    dp = [-1] * (n+1)
    dp[0] = dp[1] = 1
    for i in range(2,n+1):
        dp[i] = i * dp[i-1]
    return dp[n]
    
n = 100
ans = factorial(n)
print(ans)