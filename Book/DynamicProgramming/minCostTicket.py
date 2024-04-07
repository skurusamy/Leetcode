'''
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
'''

days = [1,4,6,7,8,20]
costs = [2,7,15]

dp =[0] * (len(days))
dp[len(days)-1] = min(costs)
for i in range(len(days)-2,-1,-1):
    #calculate d7 and d30
    d7 , d30 = i, i
    while d7 < len(days) and days[d7] < days[i] + 7:
        d7 += 1
    while d30 < len(days) and days[d30] < days[i] +30:
        d30 += 1
    dp [i] = min(dp[i+1]+costs[0],d7+costs[1],d30+costs[2])
print(dp[0])