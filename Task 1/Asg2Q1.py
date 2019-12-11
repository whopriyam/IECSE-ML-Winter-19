import numpy as np
def gen_strides(a, stride_len, window_len):
    '''
    Input:
      a: Numpy array of 1 dimension
      stride_len: int, stride length
      window_len : int, window length
    
    Output:
      Numpy array of 2 dimensions containing windowed strides as explained above
    '''
    n = 0
    for x in a:
    	n = n+1
    an = np.zeros(window_len)
    i = 0
    at = np.array([])
    while i + window_len != n + stride_len:
    	at = a[i:window_len +i]
    	an = np.vstack([an,at])
    	i = i + window_len-stride_len
    
    af = an[1:,:]
    print(af)
    return af

"""Test for strides"""
assert (np.all(gen_strides(np.array([1, 3, 7, 1, 2, 6, 0, 1]),2,4) == np.array([[1, 3, 7, 1], [7, 1, 2, 6], [2, 6, 0, 1]])))

print("Sample Tests passed", '\U0001F44D')