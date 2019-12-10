def pack(l):
	"""
	Returns a list with consecutive duplicate elements packed into sublists
	"""
	n = 0
	num = 0
	ls = []
	ln = []
	for x in l:
		n = n + 1
	if l[0] != l[1]:
		ln.append([l[0]])
	for i in range(1,n):
		if l[i] == l[i-1]:
			ls.append(l[i-1])
		else:
			ls.append(l[i-1])
			ln.append(ls)
			if i != n:
				ls = []
	ls.append(l[n-1])
	ln.append(ls)
	print(ln)
	return ln
pack([1, 1, 1, 2])
pack([1, 1, 1, 2, 1, 1, 3, 3, 3])