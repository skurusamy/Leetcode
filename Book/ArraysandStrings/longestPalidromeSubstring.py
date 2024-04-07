
st = "abbacdftg"
ans =""
ansLen =""
if st == "" and len(st) == 0:
    print("None")
for i in range(len(st)):
    #handle odd and even
    left, right = i, i
    while left >= 0 and right < len(st) and st[left] == st[right]:
        if len(ans) < (right-left+1):
            ans = st[left:right+1]
            ansLen = right - left +1
        left -= 1
        right += 1
    #even
    left, right = i, i+1
    while left >= 0 and right < len(st) and st[left] == st[right]:
        if len(ans) < (right-left+1):
            ans = st[left:right+1]
            ansLen = right - left +1
        left -= 1
        right += 1
print(ans)
