def slice(l, i, k):
	"""
	Returns a list containing the elements between i'th and k'th elements of original list l.
	"""  
	ls = []
	n = 0
	for x in l:
		n = n + 1
	if k > n:
		k = n
	for i in range(i,k):
		ls.append(l[i])
	print(ls)
	return ls
slice([1, 3, 8, 9, 7], 1, 3)
slice([1, 4, 6, 'x', 9, 0], 2, 10)