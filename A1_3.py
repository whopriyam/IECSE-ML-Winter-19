def reverse_list(l):
    m = []
    for i in l:
        m.insert(0, i)
    return m
assert reverse_list([2, 3, 4]) == [4, 3, 2]
