def compress(l):
    s = len(l)
    c = 1
    while c < s:
        if l[c - 1] == l[c]:
            l.pop(c)
            c = c - 1
            s = s - 1
        c = c + 1
    return l
assert (compress([1, 2, 2])) == [1, 2]
assert (compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x'])) == [1, 2, 1, 3, 'x']
