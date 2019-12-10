def is_palindrome(l):
    f = True
    for i in l:
        if l[-(l.index(i) + 1)] != i:
            f = False
    return f
assert (is_palindrome([1, 2, 1])) is True
assert (is_palindrome([1, 2, 3, 2, 1])) is True
assert (is_palindrome([1, 2, 3, 4])) is False
