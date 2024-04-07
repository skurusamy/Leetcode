'''
Input: arr[] = {15, 16, 10, 9, 6, 7, 17} 
Output: Range : 11 
Coefficient of Range : 0.478261 
Max = 17, Min = 6 
Range = Max – Min = 17 – 6 = 11 
Coefficient of Range = (Max – Min) / (Max + Min) = 11 / 23 = 0.478261
'''
arr =[15, 16, 10, 9, 6, 7, 17]
max_ele = max(arr)
min_ele = min(arr)
range = max_ele - min_ele
coeff = (max_ele - min_ele) / (max_ele + min_ele)
print(range,round(coeff,2))