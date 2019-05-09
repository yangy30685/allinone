import numpy as np
import matplotlib.pyplot as plt

def foo(x):
    return np.sin(x)+0.5*x
def foo_2(x):
    return np.cos(x)+x

x = np.linspace(-2*np.pi, 2*np.pi, 100)

fig_1 = plt.figure(num = 1, figsize = (15, 8), dpi = 80)

plt.plot(x, foo(x), 'k', label = 'foo(x)')
plt.plot(x, foo_2(x), 'r', label ='foo_2(x)')

# location number
# 0: ‘best' 1: ‘upper right' 2: ‘upper left' 3: ‘lower left' 4: ‘lower right' 
# 5: ‘right' 6: ‘center left'
# 7: ‘center right' 8: ‘lower center' 9: ‘upper center' 10: ‘center'

plt.legend(loc = 9, fontsize='16')
plt.grid(True)
plt.xlabel('X', fontsize='16')
plt.ylabel('f(x)', fontsize='16')

# polyfit and polyval regression（deg=1）
# y= ax+b

reg = np.polyfit(x, foo(x), deg = 1)
reg_1 = np.polyfit(x, foo(x), deg = 2)

print()
print(reg)
print()
print(reg_1)
print()

ry = np.polyval(reg, x)
ry_1 = np.polyval(reg_1, x)

fig_2 = plt.figure(num = 2, figsize = (15, 8), dpi = 80)

plt.plot(x, foo(x), 'k', label = 'foo(x)')
plt.plot(x, ry, 'r.-', label = 'regression deg=1')
plt.plot(x, ry_1, 'go', label = 'regression deg = 5')

plt.legend(loc = 'upper left', fontsize = '16')
plt.grid(True)
plt.xlabel('x axis', fontsize = '16')
plt.ylabel('foo(x)', fontsize = '16')
plt.show()
