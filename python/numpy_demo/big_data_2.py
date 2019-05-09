import numpy as np
import matplotlib.pyplot as plt

def foo(x):
    return np.sin(x) + 0.5 * x

x = np.linspace(-2 * np.pi, 2 * np.pi, 50)

reg = np.polyfit(x, foo(x), deg=1)
ry = np.polyval(reg, x)
plt.figure(1)
plt.plot(x, foo(x),'b')
plt.grid(True)
plt.xlabel('x axis')
plt.ylabel('foo(x)')

plt.figure(2)
plt.grid(True)
plt.xlabel('x axis')
plt.ylabel('fit')
plt.plot(x,ry,'r')

plt.show()

diff_1 = np.allclose(foo(x), ry)
diff_2 = np.sum((foo(x) - ry) ** 2) / len(x)
print(diff_1, diff_2)

matrix = np.zeros((4, len(x)))
print(matrix)

matrix[3, :] = x ** 3
matrix[2, :] = x ** 2
matrix[1, :] = x
matrix[0, :] = 1
print(matrix.T)