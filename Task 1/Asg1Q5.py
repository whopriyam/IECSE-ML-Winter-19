def compress(l):
    """
    Returns a list with consecutive duplicate elements replaced by a single element
    """
    n = 0;
    for x in l:
    	n = n+1
    i = 0;
    ln = [l[0]]
    for j in range(1,n):
    	if l[i] != l[j]:
    		i = j
    		ln.append(l[i])
    return ln

"""Testing code for compress"""

assert(compress([1, 2, 2])) == [1, 2]
assert(compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x'])) == [1, 2, 1, 3, 'x']
