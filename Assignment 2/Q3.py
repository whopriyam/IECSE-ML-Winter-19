import numpy as np
import os
def match(a,b):
	'''
	Inputs:
	  a, b: numpy arrays of same shape of 1 dimension
	Outputs:
	  list containing indices where both arrays have same elements
	'''
	n = 0
	for x in a:
		n = n + 1
	ls = []
	for i in range(n):
		if a[i] == b[i]:
			ls.append(i)
	print(ls)
	return ls
match(np.array([1,2,3,2,3,4,3,4,5,6]),np.array([7,2,10,2,7,4,9,4,9,8]))
ch = input("Press any key to exit...")
os.system("clear")