s = "LL"
curr = 0
for i in s:
    if i == 'U' or i == 'R':
        curr += 1
    else:
        curr -= 1
print(curr==0)