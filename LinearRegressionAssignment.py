import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('BostonHousing.csv', delimiter=',', skip_header=1)
S = data.shape
X = data[:, :S[1]-1]
Y = data[:, S[1]-1]
Y = Y.reshape((S[0], 1))
# print(X, Y)
mean = np.mean(data, axis=1)
dev = np.ptp(data, axis=1)
for i in range(S[0]):
    for j in range(S[1]):
        data[i, j] = (data[i, j] - mean[j])/dev[j]
X = np.concatenate((np.ones((S[0], 1)), X), axis=1)
T = np.zeros((S[1], 1))
# print(X, T, Y)


def cost(x, y, t):
    m = x.shape[0]
    r = np.dot(x, t) - y
    r = r*r
    return np.sum(r)/(2*m)


# print(cost(X, Y, T))
rate = 0.1
c = 0
test = [[], []]
p = 0
while True:
    T = T - rate*c/S[0]
    # print(T)
    c = np.dot(X.T, (np.dot(X, T) - Y))
    j = cost(X, Y, T)
    # print(j, '\n')
    test[0].append(p)
    test[1].append(j)
    p = p + 1
    if j < 0.00025 or p > 1000:
        break
plt.plot(test[0], test[1])
plt.show()
print(T)

