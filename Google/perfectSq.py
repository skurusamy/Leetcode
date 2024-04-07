import math,sys 
def numSquares( n):
        sqr_list = []
        for i in range(1,(int)(math.sqrt(n))+1):
            sqr_list.append(i ** 2)
        print(sqr_list)
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for square in sqr_list:
                if i < square:
                    break
                dp[i] = min(dp[i],dp[i-square]+1)
        print(dp)
        return dp[n]
n = 8
print(numSquares(n))