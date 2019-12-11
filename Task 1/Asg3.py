import matplotlib.pyplot as plt
fig,ax = plt.subplots(1)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
y = [5, 7, 8, 3, 5, 6, 3, 7, 2, 12, 5, 7, 2, 6, 9, 2]
ax.plot(x, y, 'r-')
plt.title('Epic info')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()