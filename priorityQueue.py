count = {'a': 2,'b':1,'c':8}
print(sorted(count.items(), key=lambda x:x[1],reverse=True))