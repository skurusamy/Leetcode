def climbingStairs(n):
    if n == 0 or n == 1:
        return 1
    else:
        return climbingStairs(n-1) + climbingStairs(n-2)
n = 3
print(climbingStairs(n))
