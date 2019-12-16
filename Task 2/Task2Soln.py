import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('BostonHousing.csv')

print(data.head())

data_norm = (data - data.mean())/(data.max()-data.min())

print(data_norm)

X = data_norm.iloc[:, 0:13]
ones = np.ones([X.shape[0], 1])
X = np.concatenate((ones, X), axis = 1)

Y = data_norm.iloc[:, 13:14].values
theta = np.zeros([1,14])

alpha = 0.01
iters = 1000

print(X)
def CostFunc(X,Y,theta):
	s = np.power(((X.dot(theta.T))-Y),2)
	return np.sum(s)/(2*len(X))

print(CostFunc(X,Y,theta))

def GradDesc(X,Y,theta,alpha):
	cost = np.zeros(iters)
	for i in range(iters):
		theta = theta - (alpha/len(X)) * np.sum(X * (X @ theta.T - Y), axis=0)
		cost[i] = CostFunc(X,Y,theta)

	return theta, cost

theta_g, cost = GradDesc(X,Y,theta,alpha)
print(theta_g)

finalCost = CostFunc(X,Y,theta_g)
print(finalCost)

fig, ax = plt.subplots()  
ax.plot(np.arange(iters), cost, 'b')  
ax.set_xlabel('Iterations')  
ax.set_ylabel('Cost')  
ax.set_title('Drop in Cost Function')  
plt.show()

pred = np.dot(theta_g,X.T)
print(pred)

num_train = 405
num_test = 101

X_train = data_norm.iloc[0:405,0:13]
ones = np.ones([X_train.shape[0],1])
X_train = np.concatenate((ones,X_train), axis = 1)
Y_train = data_norm.iloc[0:405,13:14].values
X_test = data_norm.iloc[405:507, 0:13]
ones = np.ones([X_test.shape[0],1])
X_test = np.concatenate((ones,X_test), axis = 1)
Y_test = data_norm.iloc[405:507,13:14].values

print(CostFunc(X_train,Y_train,theta))

theta_g1, cost1 = GradDesc(X_train, Y_train, theta, alpha)
print(theta_g1)

finalCost = CostFunc(X_train, Y_train, theta_g1)
print(finalCost)

pred = np.dot(theta_g1,X_train.T)
print(pred.T, '  ', Y_train)