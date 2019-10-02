import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 
def func(x, a, b, n):
    return a * np.power(x, n) + b
 
# xdata = np.linspace(0, 2, 500)
# ydata = -2 * np.power(xdata, 3) + 10
xdata = [0,10,30,36]
ydata = [10,9.5,6,4]

# np.random.seed(2019)
# y_noise = .5* np.random.normal(size = xdata.size)
# ydata = ydata + y_noise

fig_1 = plt.figure(1)
plt.plot(xdata, ydata, label = 'Temp', linestyle = '--', color = 'k',
marker = 'x', markeredgecolor = '0.10', markerfacecolor = '0.75')

# Fit for the parameters a, b of the function func:
# popt, pcov = curve_fit(func, xdata, ydata)
# Constrain the optimization to the region of -1000 <= a <= 0, -1000 <= b <= 10 ,0<n<5:
popt, pcov = curve_fit(func, xdata, ydata, bounds=([-1000,-1000,0], [0., 10.,5]))
print(f'the fitting coefficient is : {popt}')

xdata_fit = np.linspace(0, 36, 100)
plt.plot(xdata_fit, func(xdata_fit, *popt), color='r', linestyle='-',
label='fit_coef: a=%10.8f, b=%10.5f,n=%10.5f' % tuple(popt))

plt.xlabel('time')
plt.ylabel('Degree Celsius')
plt.legend()
plt.show()


# #Define the data to be fit with some noise:
# xdata = np.linspace(0, 360, 50)
# y = func(xdata, 2.5, 1.3)
# np.random.seed(1729)
# y_noise = 0.2 * np.random.normal(size=xdata.size)
# ydata = y + y_noise
# plt.plot(xdata, ydata, 'b-', label='data')
 
# #Fit for the parameters a, b, c of the function func:
# popt, pcov = curve_fit(func, xdata, ydata)
# print(popt)
# plt.plot(xdata, func(xdata, *popt), 'r-',
# label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
 
# #Constrain the optimization to the region of 0 <= a <= 3, 0 <= b <= 1 and 0 <= c <= 0.5:
# popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
# print(popt)
# plt.plot(xdata, func(xdata, *popt), 'g--',
# label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))