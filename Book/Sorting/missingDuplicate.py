arr = [1,2,3,4,5,5]
ans = [False] * len(arr)
for i in arr:
    if ans[i-1] == False:
        ans[i-1] = True
#find duplicate
    else:
        print("Duplicate:",i)
        break
print(ans,arr)
for j in range(len(arr)):
    if ans[j] == False:
        print("Missing:",j+1)
        break
