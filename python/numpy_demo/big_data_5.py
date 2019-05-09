import numpy as np
import matplotlib.pyplot as plt

xn = np.linspace(-2*np.pi, 2*np.pi, 50)

xtemp = np.random.standard_normal(len(xn))

plt.figure(1)
plt.plot(xn, xtemp,'r-.')

# print(xtemp)
# xn = xn + 0.15 *xtemp
# print(xn)

def f(x):
    return np.sin(x) + 0.5 * x

# add noise on xn
xn = xn + 0.15 * xtemp

# add noise on yn 
yn = f(xn) + 0.5 * xtemp

plt.figure(2)
plt.plot(xn, yn, 'k^')

plt.show()