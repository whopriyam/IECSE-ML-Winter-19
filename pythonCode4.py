def is_palindrome(l):
    p=list()
    for i in l:
        p.append(i)
    l.reverse()
    print(l)
    print(p)
    if p == l:
        return True
    else:
        return False
