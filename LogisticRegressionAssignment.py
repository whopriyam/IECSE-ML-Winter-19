import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('Logistic Regression Assignment\\train1.csv', delimiter=',', skip_header=1)
S = data.shape
X = np.concatenate((np.ones((S[0], 1)), data[:, 2].reshape((S[0], 1)), data[:, 5:9], data[:, 10].reshape((S[0], 1)), data[:, 12].reshape((S[0], 1))), axis=1)
X = np.nan_to_num(X)
Y = data[:, 1]
Y = Y.reshape((S[0], 1))
m = X.shape[0]
n = X.shape[1]
# print(Y)
# print(X)
T = np.zeros((n, 1))
# print(X, T, Y)


def sig(p):
    return 1/(1+np.exp(-p))


def hypo():
    return sig(np.dot(X, T))
# print(hypo())


def cost():
    return -1/m * np.sum(Y * np.log(hypo()) + (1 - Y) * (np.log(1 - hypo())))
# print(cost())


def grad():
    return np.dot(X.T, (hypo() - Y))/m
# print(grad())


rate = 0.1
test = [[], []]
p = 0
while True:
    J = cost()
    T = T - grad()
    # print(grad(), '\n')
    # print(T)
    # print(J, '\n')
    test[0].append(p)
    test[1].append(J)
    p = p + 1
    if J < 0.00025 or p > 200:
        break
# plt.plot(test[0], test[1])
# plt.show()
# print(T)
