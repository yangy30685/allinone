import numpy as np
import matplotlib.pyplot as plt

s = (4,3)
arr_1 = np.zeros(s,dtype = np.int8)
arr_2 = np.zeros(s,dtype = np.float64)

print(arr_1)
print(arr_2)

s = (4,3)
arr_1 = 0.0009 * np.ones(s, dtype = np.float16)
arr_2 = 0.00009 * np.ones(s, dtype = np.float64)

print(arr_1)
print(arr_2)

# create value
x = np.linspace(-1, 1, 50)
y1 = 2*x+1
y2= 10*x**2

# create a figure
plt.figure(figsize=(10,10))
# careful with comma here
l1, = plt.plot(x,y1,label='line')
l2, = plt.plot(x,y2,label='parabola',color = 'red', linewidth = 1.0, linestyle = '--')

# set axis range
plt.xlim(-1,1)
plt.ylim(-2,10)

# set axis label
plt.xlabel('x axis')
plt.ylabel('y axis')

# set x axis marker
plt.xticks(np.linspace(-1,1,20))

# set y marker a
# $$ is font style
# plt.yticks([-1, 1, 3], ['$minium$', 'normal','demo marker'])
plt.yticks(np.linspace(-2, 10, 20))

# set legend
plt.legend(handles = [l1, l2,], labels = ['a', 'b'], loc = 'best')
plt.show()