def insert_element(l, i, elem):
	"""
	Returns a new list containing elem at index i. If i > len (l), insert element at the end of the list
	"""      
	n = 0
	for x in l:
		n = n + 1
	if i > n:
		l.append(elem)
	else:
		l.insert(i,elem)
	print(l)
	return l
insert_element([1, 2, 3, 4,], 2, 5)
insert_element([1, 5, ], 3, 5)