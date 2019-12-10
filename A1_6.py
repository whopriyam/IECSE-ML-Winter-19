def pack(l):
    final = [[]]
    c = 0
    final[0].append(l[0])
    for i in range(1, len(l)):
        if l[i] != final[c][0]:
            final.append([])
            c = c + 1
        final[c].append(l[i])
    return final

assert(pack([1, 1, 1, 2]) == [[1, 1, 1], [2]])
assert(pack([1, 1, 1, 2, 1, 1, 3, 3, 3]) == [[1, 1, 1], [2], [1, 1], [3, 3, 3]])
