num = int(input("Enter n stair: "))
ans = [0] * (num+1)
ans[0]=1
ans[1]=1
for i in range(2,num+1):
    ans[i] = ans[i-1]+ans[i-2]
print(ans)
print(ans[num])