def isBalanced(arr):
    stack = []
    for i in arr:
        if i == '{' or i == '[' or i == '(':
            stack.append(i)
        if i == '}':
            stack.pop()
            if i == ')' or i == ']':
                return False
        elif i ==')':
            stack.pop()
            if i == '}' or i == ']':
                return False
        elif i ==']':
            stack.pop()
            if i == '}' or i == ')':
                return False
    if len(stack) == 0:
        return True


arr = "{}{}[{]"
if isBalanced(arr):
    print("Balanced")
else:
    print("Not Balanced")