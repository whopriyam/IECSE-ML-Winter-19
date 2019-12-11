def reverse_list(l):
    """
    Returns the reverse of a list l
    """
    n = 0
    for x in l:
    	n = n + 1
    n1 = (int)(n/2)
    for i in range(n1):
    	t = l[i]
    	l[i] = l[n-1-i]
    	l[n-1-i] = t
    return l


assert reverse_list([2, 3, 4])== [4, 3, 2]