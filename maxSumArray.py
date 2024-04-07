#n = int(input("Enter the size of an array: "))
'''
Max sum in an array
not max subarray

'''
arr = [2,3,5,-7,8,-1,9]
#for i in range(len(arr)):
#   arr.append(int(input()))
curr_max = 0
for i in arr:
    curr_max = max(curr_max, curr_max + i, i)
print(curr_max)