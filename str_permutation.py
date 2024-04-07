def toString(st):
    return "".join(st)


def permutation(st, l, r):
    if l == r:
        print(toString(st))
    else:
        for i in range(l, r + 1):
            st[l], st[i] = st[i], st[l]
            permutation(st, l + 1, r)
            st[l], st[i] = st[i], st[l]


st = "avc"
st1 = list(st)
permutation(st1, 0, len(st) - 1)
