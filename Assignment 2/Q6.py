import numpy as np
import os
def rankArray(arr):
	'''
	Input:
	    arr: Numpy array of arbitrary dimensions 
	Output:
	    numpy array of same shape as arr but with elements replaced by their ranks
	'''
	n = np.size(arr,1)
	m = np.size(arr,0)
	r = np.size(arr)
	ls = []
	for i in range(m):
		for j in range(n):
			ls.append(arr[i,j])
	ls.sort()
	t = np.zeros(n)
	ar = np.zeros(n)
	for i in range(m):
		for j in range(n):
			for k in range(r):
				if arr[i,j] == ls[k]:
					t[j] = k
					ls[k] = 'x'
					break
		ar = np.vstack([ar,t])
	a = ar[1:,:]
	print(a)
	return a
rankArray(np.array([[9, 4, 15, 0, 17], [16,17,8,9,0]]))
ch = input("Press any key to exit...")
os.system("clear")