def isBalanced(exp):
    stack =[]
    for i in range(len(exp)):
        if exp[i] == '{' or exp[i] == '[' or exp[i] == '(':
            stack.append(exp[i])
        else:
            x = stack.pop()
            if exp[i] == '}':
                if x == '[' or x == '(':
                    return False
            elif exp[i] == ')':
                if x == '[' or x == '{':
                    return False
            else:
                if x == '{' or x == '(':
                    return False
    return True


exp = "{([()])}"
print(isBalanced(exp))
