def insert_element(l, i, elem):
    """
    Returns a new list containing elem at index i. If i > len (l), insert element at the end of the list
    """    
    n = 0
    ln = []
    for x in l:
    	n = n+1  
    if i>n:
    	i = n
    	ln += l
    	ln.append(elem)
    else:
    	for j in range(n):
    		if j == i:
    			ln.append(elem)
    		ln.append(l[j])
    return ln

"""Testing code for insert_element"""
assert(insert_element([1, 2, 3, 4,], 2, 5)[2]) == 5
assert(insert_element([1, 5, ], 3, 5)) == [1, 5, 5]
