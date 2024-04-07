def fib(n):
    ans = [0] * (n+1)
    ans[0] = 0
    ans[1] = 1
    for i in range(2,n+1):
        ans[i] = ans[i-1] + ans[i-2]
    print(ans)
    print(ans[n])
n = 10
fib(n)