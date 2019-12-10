import numpy as np

def lin_eqn(a,b):
    a_inv = np.linalg.inv(a)
    x = np.dot(a_inv, b)
    return x


"""Test for lin_eqn"""
assert np.any(lin_eqn(np.array([[1, 2], [3, 4]]), np.array([8, 18])) == np.array([2., 3.]))

print("Sample Tests passed", '\U0001F44D')