import numpy as np
import os
def shuf(arr):
	'''
	Input: 
	arr: Numpy array of arbitrary number of dimensions (>1)
	Output:
	numpy array of same shape as arr but with rows shuffled
	'''
	np.random.shuffle(arr)
	print(arr)
	print(np.shape(arr))
	return arr
shuf(np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
ch = input("Press any key to exit...")
os.system("clear")