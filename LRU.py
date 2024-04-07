cache_size = int(input("Enter the cache size: "))
op = int(input("Enter number of operations: "))
key_l = []
value_l = []
while op > 0:
    st = input("Enter G  or P : ")
    if st == 'P':
        key = int(input("Enter key: "))
        val = int(input("Enter value: "))
        if len(key_l) == cache_size:
            key_l.remove(key_l[0])
            value_l.remove(value_l[0])
        key_l.append(key)
        value_l.append(val)
    elif st == 'G':
        key = int(input("Enter the key value: "))
        if key in key_l:
            ind = key_l.index(key)
            print("The value is "+ str(value_l[ind]))
        else:
            print("Not Found")
    print(key_l)
    print(value_l)
    op -=1