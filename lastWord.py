str = input("Enter the string: ")
count = 0;
for i in range(len(str)-1,-1,-1):
    if str[i] != ' ':
        count +=1
    else:
        break
print(count)