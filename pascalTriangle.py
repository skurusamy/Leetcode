n = 5
ans = []
i = 0
while i < n:
    res =[-1] * (i +1)
    res[0] = res[i] = 1
    j = 1
    while j < i:
        res[j]  = ans[i-1][j-1] + ans[i-1][j]
        j += 1
    ans.append(res)
    i += 1
print(ans)
