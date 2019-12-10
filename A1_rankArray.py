import numpy as np

def rankArray(arr):
    '''
    Input:
        arr: Numpy array of arbitrary dimensions 
    Output:
        numpy array of same shape as arr but with elements replaced by their ranks
    '''
    # YOUR CODE HERE
    a = []
    for i in arr:
        for j in i:
            a.append(j)
    a.sort()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            k = a.index(arr[i][j])
            arr[i][j] = k
            a[k] = -1
    return arr

"""Test for rankArray"""
assert np.all(rankArray(np.array([[9, 4, 15, 0, 17], [16,17,8,9,0]])) == np.array([[4,2, 6, 0, 8], [7, 9, 3, 5, 1]]).tolist())
print("Sample Tests passed", '\U0001F44D')