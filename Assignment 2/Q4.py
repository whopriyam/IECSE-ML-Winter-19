import numpy as np
import os
def inv(arr):
	"""
	Given an array arr (square matrix), find its inverse
	"""
	if(arr.shape[0]==arr.shape[1]):
		i=np.eye(arr.shape[0])
		print(np.linalg.inv(arr))
		return np.linalg.inv(arr)
inv(np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]]))
ch = input("Press any key to exit...")
os.system("clear")