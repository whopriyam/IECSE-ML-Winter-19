def compress(l):
	"""
	Returns a list with consecutive duplicate elements replaced by a single element
	"""
	n = 0
	ls = []
	for x in l:
		n = n + 1
	for i in range(1,n):
		if l[i] != l[i-1]:
			ls.append(l[i-1])
	ls.append(l[n-1])
	print(ls)
	return ls
compress([1, 2, 2])
compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x'])