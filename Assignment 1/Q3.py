def reverse_list(l):
	"""
	Returns the reverse of a list l
	"""
<<<<<<< HEAD
	# YOUR CODE HERE
	rl = []
=======
>>>>>>> eaef142a271ad36569cec121e754e05c05f4a293
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
<<<<<<< HEAD
reverse_list([2, 3, 4])
=======
reverse_list([2, 3, 4])
>>>>>>> eaef142a271ad36569cec121e754e05c05f4a293
