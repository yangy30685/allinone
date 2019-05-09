import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
# find the root of the polynomial f(x) = 2x^2+3x-10
def f(x):
    y = 2.0 * x**2 + 3.0*x -10.0
    return y

x = np.linspace(-5,3,2000)

plt.figure(1)

plt.plot(x,f(x),'b')
plt.plot(x,np.zeros(len(x)))

plt.xlabel('x axis')
plt.ylabel('f(x)')

plt.grid(True)
plt.show()

x1 = fsolve(f,1.0)
x2 = fsolve(f,-2.0)
print(x1,'\n',x2)


# find the root of the polynomial f(x,y) = 2x^2/3+y2/3-9^1/3 g(x,y)=x^2/4+u^.5-1
# initial guess x0=1 y0=1

def f2(z):
    x = z[0]
    y = z[1]
    f = np.zeros(2)

    f[0] = 2.0*x**(2.0/3.0) + y**(2.0/3.0) - 9.0**(1.0/3.0)
    f[1] = x**2.0/4.0 + y**(0.5) - 1.0
    return f

print(f2([.1,.1]))

# find the root of the f2(z)=0
z = fsolve(f2, [1.0,1.0])
print(z)
print(f2(z))