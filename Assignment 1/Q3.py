def reverse_list(l):
	"""
	Returns the reverse of a list l
	"""
	n = 0
	temp = 0
	for x in l:
		n = n + 1
	for i in range(int(n/2)):
		temp = l[i]
		l[i] = l[n-1-i]
		l[n-1-i] = temp
		print(l)
	return l
reverse_list([2, 3, 4])
