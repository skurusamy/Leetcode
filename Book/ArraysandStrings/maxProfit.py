prices = [7,1,5,3,6,4]
#prices = [1,2,3,4,5]
profit =0
for i in range(len(prices)-1):
    if prices[i] < prices[i+1]:
        profit += prices[i+1] - prices[i]
print(profit)