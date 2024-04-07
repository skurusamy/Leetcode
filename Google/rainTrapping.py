
def trap(height):
    if len(height) < 3:
        return 0
    dp =[0] * len(height)
    left_max =[height[0]] * len(height)
    right_max =[height[len(height)-1]] * len(height)
    for i in range(1,len(left_max)):
        left_max[i] = max(left_max[i-1],height[i])
    for i in range(len(left_max)-2,-1,-1):
        right_max[i] = max(right_max[i+1],height[i])
    for i in range(len(height)):
        ans = min(left_max[i],right_max[i]) - height[i]
        if ans > 0:
            dp[i] = ans
    print(left_max,right_max, height,dp)
    return sum(dp)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))