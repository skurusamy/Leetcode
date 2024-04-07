Arr = [1,2,3,0]
target = 3
count = {}
for num in Arr:
    if num not in count:
        count[num] = 1
    else:
        count[num] = count[num] + 1
second_val = 0
print(count)
for i in range(len(Arr)):
    val = target - Arr[i]
    if val in count:
        second_val += count[val]
    if val == Arr[i]:
        second_val = second_val-1
print(second_val//2)