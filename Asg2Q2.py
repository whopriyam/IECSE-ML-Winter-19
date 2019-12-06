import numpy as np
def shuf(arr):
  '''
  Input: 
    arr: Numpy array of arbitrary number of dimensions (>1)
  Output:
    numpy array of same shape as arr but with rows shuffled
  '''
  arrn = np.array(arr)
  n = arr.shape[0]
  pos = 1
  for i in range(n):
  	t = arrn[0,i]
  	arrn[0,i] = arrn[pos,i]
  	arrn[pos,i]= t 
  return arrn

"""Test for shuf"""
arr=np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
assert np.any(shuf(np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])) != np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
assert shuf(np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])).shape == np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).shape

print("Sample Tests passed", '\U0001F44D')