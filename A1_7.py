def slice(l, i, k):
    m = []
    if k > len(l):
        k = len(l)
    for j in range(i, k):
        m.append(l[j])
    return m

assert(slice([1, 3, 8, 9, 7], 1, 3)) == [3, 8]
assert(slice([1, 4, 6, 'x', 9, 0], 2, 10)) == [6, 'x', 9, 0]
