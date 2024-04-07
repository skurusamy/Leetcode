def countSpaces(st,trueLength):
    count = 0
    for i in range(0,trueLength):
        if st[i] == ' ':
            count += 1
    return count

def urlify(st,trueLength):
    #find number of spaces in original String
    num_Spaces=countSpaces(st,trueLength)
    newIndex = trueLength -1 + (num_Spaces * 2)
    st = list(st)
    if newIndex > trueLength +1:
        st[newIndex] = None
    for i in range(trueLength-1,-1,-1):
        if st[i] == ' ':
            st[newIndex] = '0'
            st[newIndex-1] = '2'
            st[newIndex-2] = '%'
            newIndex -= 3
        else:
            st[newIndex] = st[i]
            newIndex -= 1
    st1 =" "
    for i in st:
        st1 += i
    return st1
st = 'Hello my dear Family      '
trueLength = 20
print(urlify(st,trueLength))