'''
8
UDDDUDUU
output: 1
'''

steps = input("Enter the string: ")
sealevel = valley = 0
for i in steps:
    if i == 'U':
        sealevel += 1
    if i == 'D' :
        sealevel -= 1
    if i == 'U' and sealevel == 0:
        valley += 1
print(valley)