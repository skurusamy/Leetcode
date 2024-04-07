'''
https://www.youtube.com/watch?v=lXVy6YWFcRM
'''

arr = [6, -3, -10,0,1]
result = max(arr)
max_product = 1
min_product = 1
for i in arr:
    if i == 0:
        result = max(max_product,min_product)
        max_product = 1
        min_product = 1
        continue
    tmp = max_product
    max_product =  max(i, i * max_product , i * min_product)
    min_product = min(i, i * tmp , i * min_product)
    result = max(max_product,min_product,result)
print(result)
