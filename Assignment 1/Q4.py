def is_palindrome(l):
	"""
	Returns True if l is a palindrome, False otherwise
	"""
	f = 0
	n = 0
	for x in l:
		n = n + 1
	for i in range(n):
		if l[n-1-i] != l[i]:
			f = 1
	if f == 0:
		print("True")
	else:
		print("False")
is_palindrome([1, 2, 1])
is_palindrome([1, 2, 3, 2, 1])
is_palindrome([1, 2, 3, 4])