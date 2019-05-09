import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import seaborn

# devide 1 sec into 1400 sample points
# the smaple frequency must be 2times bigger than sin frequency 

x = np.linspace(0,1,1400)
# x = np.arange(0,2*np.pi,np.pi/300)
# print(x)

# set sin frequencey to be 180，390和600
# y=7*np.sin(2*np.pi*180*x) + 2.8*np.sin(2*np.pi*390*x)+5.1*np.sin(2*np.pi*600*x)
y=np.sin(2*np.pi*180*x)+2.8*np.sin(2*np.pi*390*x)+np.sin(2*np.pi*600*x)
# print(y)

# fig_1 = plt.plot(x[0:50],y[0:50]) 
# plt.show(fig_1)
yy=fft(y)                     # fourier transform
yreal = yy.real               # get real part
yimag = yy.imag               # get virtual part

yf=abs(fft(y))                # get absolute value
# print(max(yf))
yf1=yf/len(x)                 # normalise
# print(int(len(x)/2))
yf2 = yf1[:int(len(x)/2)]     # take half part due to symmetry 

xf = np.arange(len(x))        # (0, 1,2,... 1399)
# print(xf)
xf1 = xf
xf2 = np.arange(len(x)/2)     # onyl take half section
# print(type(len(y)/2))
plt.subplot(411)
plt.plot(x[0:100],y[0:100])   
plt.title('Original wave')

plt.subplot(412)
plt.plot(xf,yf,'r')
plt.title('FFT of Mixed wave(two sides range)',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表

plt.subplot(413)
plt.plot(xf1,yf1,'g')
plt.title('FFT of Mixed wave(normalization)',fontsize=9,color='k')

plt.subplot(414)
plt.plot(xf2,yf2,'b')
plt.title('FFT of Mixed wave(single sides range ))',fontsize=10,color='k')

plt.show()