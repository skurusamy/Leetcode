amount = 10
coins =[1,5,10,25,50,100]
ans =[0] * (amount+1)
ans[0] = 1
for i in coins:
    for j in range(i,amount+1):
        ans[j] = ans[j] + ans[j-i]
print(ans[amount])