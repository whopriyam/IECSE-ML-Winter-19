import numpy as np
import os
os.system("clear")
def gen_strides(a, stride_len, window_len):
	'''
	Input:
	  a: Numpy array of 1 dimension
	  stride_len: int, stride length
	  window_len : int, window length

	Output:
	  Numpy array of 2 dimensions containing windowed strides as explained above
	'''
	arr = np.zeros(window_len)
	t = np.array([])
	for x in a:
		n = n + 1
	while i + window_len != n + stride_len:
		t = a[i:window_len + i]
		arr = np.vstack([arr,t])
		i = i + window_len - stride_len
	ar = arr[1:,:]
	print(ar)
	return ar
gen_strides(np.array([1, 3, 7, 1, 2, 6, 0, 1]),2,4)
ch = input("\nPress any key to exit...")
os.system("clear")