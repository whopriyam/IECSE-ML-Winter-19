def slice(l, i, k):
    """
    Returns a list containing the elements between i'th and k'th elements of original list l.
    """  
    n = 0;
    for x in l:
    	n = n+1;
    if k>n:
    	k = n
    ln = []
    for j in range(i,k):
    	ln.append(l[j]);
    return ln

"""Testing code for slice"""
assert(slice([1, 3, 8, 9, 7], 1, 3)) == [3,8]
assert(slice([1, 4, 6, 'x', 9, 0], 2, 10)) == [6, 'x', 9, 0]