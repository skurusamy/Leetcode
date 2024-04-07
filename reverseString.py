s1 = "Helllo Subhu"
ans =""
for i in range(len(s1)-1,-1,-1):
    ans += "".join(s1[i])
#ans += "".join(sorted(s1.lower()))
print(ans)