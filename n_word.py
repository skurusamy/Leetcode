a = int (input(" enter a num"))
e=a
#b = int (input (" num of times "))
c = 0
d=0
while(a>0):
    c=a%10
    d=d*10+c
    a = a//10
if (d==e):
    print("palin madam")
else:
    print ("not madam")
'''a = input("Enter a num")
print(len(a))'''
