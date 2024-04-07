'''
Given numbers "23"-  create combination of letters from 2 and 3 in phone pad
'''
ip = "2"
phonePad =["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
result =[]
#base condition
if(ip == None or len(ip) == 0):
    print(result)
else:
    first = list(phonePad[int(ip[0])])
    for i in range(1,len(ip)):
        letters = phonePad[int(ip[i])]
        for j in letters:
            for k in first:
                result.append(j+k)
        first = result.copy()
        result =[]
print(first)
