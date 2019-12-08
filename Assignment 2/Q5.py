import numpy as np
import os
def lin_eqn(a,b):
	'''
	Solve the system of linear equations
	of the form ax = b

	Eg. 

	Solve the system of linear equation

	x + 2*y = 8
	3*x + 4*y = 18

	Given inputs a and b represent coefficients and constant of linear equation respectively

	coefficients: 
	a = np.array([[1, 2], [3, 4]]) 

	constants: 
	b = np.array([8, 18])

	Desired Output: [2,3]


	'''
	print(np.dot(np.linalg.inv(a),b))
	return np.dot(np.linalg.inv(a),b)
lin_eqn(np.array([[1.0, 2.0], [3, 4]]),np.array([8.0,  18.0]))
ch = input("Press any key to exit...")
os.system("clear")