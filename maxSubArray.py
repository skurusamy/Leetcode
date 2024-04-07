arr = [1,12,-2,-10,-5,-6,1,15]
max_val = 0
result = max(arr)
for i in arr:
    if i >= 0:
        max_val = max(max_val , max_val+i , i)
    else:
        result = max(max_val,result)
        max_val = 0
result = max(result,max_val)
print(result)
