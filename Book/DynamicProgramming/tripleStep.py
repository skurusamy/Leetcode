def tripleSteps(n):
    if n <0:
        return -1
    if n == 1:
        return 1
    ans = [0] *(n+1)
    ans[1] = 1
    ans[2] = 2
    ans[3] = 3
    for i in range(4,n+1):
        ans[i] = ans[i-1] + ans[i-2] + ans[i-3]
    print(ans)
    print(ans[n])

n = 10
tripleSteps(n)