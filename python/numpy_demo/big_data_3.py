import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(num = 1, figsize = (15, 8), dpi = 80)

x_1 = np.arange(0, 1, 0.1)
y_1 = range(0, 10, 1)

print(x_1)
print(y_1)
plt.plot(x_1, y_1)

x_2 = np.arange(2, 3, 0.1)
y_2 = range(0, 20, 2)

print(x_2)
print(y_2)

plt.plot(x_2, y_2)

fig = plt.figure(num=3, figsize=(15, 8),dpi=80)
ax1 = fig.add_subplot(2,1,1)  
ax2 = fig.add_subplot(2,1,2)

ax1.plot(np.arange(0,1,0.1),range(0,10,1),color='k')
ax1.plot(np.arange(0,1,0.1),range(0,20,2),color='b')
ax2.plot(np.arange(0,1,0.1),range(0,20,2),color='r')

plt.show()
