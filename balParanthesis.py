def isBalanced(s):
    st = []
    if len(s) == 0:
        return False
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            st.append(s[i])
        if s[i] == ')':
            x = st.pop()
            if x == '{' or x == '{':
                return False
        elif s[i] == '}':
            x = st.pop()
            if x == '(' or x== '[':
                return False
        elif s[i] == ']':
            x = st.pop()
            if x == '{' or x == '(':
                return False
    if len(st) != 0:
            return False
    else:
            return True



# main
expr = ")[]}"
if(isBalanced(expr)):
    print("Balanced")
else:
    print("Not balanced")