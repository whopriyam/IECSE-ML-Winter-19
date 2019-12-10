import numpy as np
import random

def shuf(arr):
    for i in range(random.randint(2, 5)):
        a = random.sample(range(0, len(arr)), 2)
        t = arr[a[0]]
        arr[a[0]] = arr[a[1]]
        arr[a[1]] = t
    return arr


"""Test for shuf"""
arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
assert np.any(shuf(np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])) != np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
assert shuf(np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])).shape == np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).shape

print("Sample Tests passed", '\U0001F44D')