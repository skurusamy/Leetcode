num = 10004
l=""
while(num):
    rem = num % 10
    if rem == 0:
        l += "5"
    else:
        l += str(rem)
    num = num //10
ans = l[len(l)-1::-1]
print(ans)
print(type(ans))