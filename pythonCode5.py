def compress(l):
    t=list()
    t.append(l[0])
    for i in range(1,len(l)):
        if l[i] is not l[i-1]:
            t.append(l[i])
    l=t
    return l
