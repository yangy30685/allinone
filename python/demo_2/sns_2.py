#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

fig_1 = plt.figure(1)

ax_1 = fig_1.add_subplot(2, 2, 1)
x_normal = np.random.randn(100)

plt.plot(x_normal,'k--')

ax_2 = fig_1.add_subplot(2, 2, 2)
ax_2.hist(x_normal, bins = 20, color = 'r', alpha = 1)

ax_3 = fig_1.add_subplot(2, 2, 3)
x_cruve = np.linspace(-10,10,50)
y_cruve = x_cruve**2
plt.plot(x_cruve, y_cruve,'b^')


fig_2 = plt.figure(2)

labels = 'AA','BB','CC','DD'

# total is 100
sizes = [10, 30, 40, 20]
# set section color
colors = ['y', 'g', 'lightskyblue', 'red']
# set the gap size
explode = (0.05, 0.2, 0.1, 0.05)

ax_1 = plt.pie(sizes, explode = explode, 
    labels = labels, colors=colors,
    autopct='%1.1f%%', shadow=True,
    startangle=90)
    # startangle contrl helix shape
plt.axis('equal')

# figure 3 
fig_3 = plt.figure(3)
ax_3 = plt.plot(np.linspace(1,10,100))

plt.show()

help(plt)