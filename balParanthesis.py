def balParanthesis(s):
    if len(s) ==0:
        return True
    stack =[]
    for x in s:
        if x == '[' or x == '(' or x == '{':
            stack.append(x)
        else:
            y = stack.pop()
            if x == '}' and y == '{':
                return True
            elif x == ']' and y == '[':
                return True
            elif x == '}' and y == '{':
                return True
    return False



s = "([{{}}])"
print(balParanthesis(s))