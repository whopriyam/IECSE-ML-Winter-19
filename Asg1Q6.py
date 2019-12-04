def pack(l):
    """
    Returns a list with consecutive duplicate elements packed into sublists
    """
    n = 0
    for x in l:
    	n = n+1
    ln = []
    lt = []
    i = 0;
    for j in range(n):
    	if l[i]==l[j]:
    		lt.append(l[j])
    	elif l[i]!=l[j]:
    		ln.append(lt)
    		i = j
    		lt = []
    		lt.append(l[j])
    ln.append(lt)
    return ln

"""Testing code for pack"""
assert(pack([1, 1, 1, 2]) == [[1, 1, 1], [2]])
assert(pack([1, 1, 1, 2, 1, 1, 3, 3, 3])) == [[1, 1, 1], [2], [1, 1], [3, 3, 3]]