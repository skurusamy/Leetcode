'''
arr[] = {10, 5, 3, 4, 3, 5, 6}
Find the first repeating element in an array of integers
'''
arr = [10, 5, 3, 4, 3, 5, 6]
newArr =[]
for i in arr:
    if i not in newArr:
        newArr.append(i)
    else:
        print(i)
        break