def palindrome_failed(st):
    l=[]
    for i in range(len(st)):
        if st[i] in l:
            l.remove(st[i])
        else:
            l.append(st[i])
    #print(l)
    if len(l) == 0 or len(l) == 1:
        return "Palindrome"
    else:
        return "No"

def correct_fn(st):
    left = 0
    flag = 0
    right=  len(st) -1
    while(left != right):
        if st[left] == st[right]:
            continue
        else:
            flag = 1
            break;
    if flag == 0:
        return "Palindrome"
    else:
        return "No"
##main
st = input("Enter the string ")
print(palindrome_failed(st))
print(correct_fn(st))