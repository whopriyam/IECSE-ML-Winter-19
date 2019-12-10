def match(a,b):
    m=list()
    for i in range(len(a)):
        if a[i]==b[i]:
            m.append(i)
    return m
