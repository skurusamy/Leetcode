ip = [1,2,3,4,5]
'''
The output array should contain product of other elements in the array
-- no divison operator allowed.
'''
left_prod =[0]*len(ip)
output = [0]*len(ip)
right_prod = [0]*len(ip)
#right_prod =[0]*len(ip)
left_prod[0]=ip[0]
right_prod[len(ip)-1] = ip[len(ip)-1]
for i in range(1,len(ip)):
    left_prod[i] = left_prod[i-1]* ip[i]
for i in range(len(ip)-2,-1,-1):
    right_prod[i] = right_prod[i+1] * ip[i]
print(left_prod,right_prod)
j = 1
output[0] =  right_prod[1]
for i in range(1,len(ip)-1):
    output[i] = left_prod[i-1] * right_prod[i+1]
output[i+1] = left_prod[len(ip)-2] 
print(output)