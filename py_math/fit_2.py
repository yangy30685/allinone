import numpy as np
import matplotlib.pyplot as plt

a = [-4,-3,-2,-1,0,1,2,3,4,5]
x = np.array(a)
y = np.array(2*(x**4) + x**2 + 9*x + 2) 

fig_1 = plt.figure(1)
plt.plot(x, y,color = 'red',linewidth = 2.0, linestyle = '--')


fig_2 = plt.figure(2)
plt.subplot(2,3,1)
coef_1 = np.polyfit(x, y, 1)
poly_fit_1 = np.poly1d(coef_1)
plt.plot(x, poly_fit_1(x), '-g',label="1st order")
print(poly_fit_1)

plt.subplot(2,3,2)
coef_2 = np.polyfit(x,y, 2)
poly_fit_2 = np.poly1d(coef_2)
plt.plot(x, poly_fit_2(x), '-b',label="2nd order")
print(poly_fit_2)

plt.subplot(2,3,3)
coef_3 = np.polyfit(x,y, 3)
poly_fit_3 = np.poly1d(coef_3)
plt.plot(x, poly_fit_3(x), '-y',label="3rd order")
print(poly_fit_3)

plt.subplot(2,3,4)
coef_4 = np.polyfit(x,y, 4)
poly_fit_4 = np.poly1d(coef_4)
plt.plot(x, poly_fit_4(x), '-k',label="4th order")
print(poly_fit_4)

plt.subplot(2,3,5)
coef_5 = np.polyfit(x,y, 5)
poly_fit_5 = np.poly1d(coef_5)
plt.plot(x, poly_fit_5(x), '-o', label="5th order")
print(poly_fit_5)


plt.show()