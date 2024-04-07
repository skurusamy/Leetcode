#1,5,10,25
coin = [1,5,10,25]
num = int(input("Enter the amount: "))
ans = [0]*(num+1)
ans[0]=1
for i in coin:
    for j in range(i,num+1):
        ans[j] = ans[j] + ans[j-i]
print(ans)
print(ans[num])