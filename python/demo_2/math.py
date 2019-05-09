#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt

# dictionary key-value
table = {'Dont worry': 4127, 'Jack': 4098, 'Dcab': 76745458}
print(table)

for m, n in table.items():
    # f format python 3.6 and later
    # print (f'{m:20} -> {n:20d}')
    print("{:15}<--->{:20}".format(m, n))

# another way to format 
for x in range(10):
    # use end modify newline
    print(repr(x).rjust(4), repr(x*x).rjust(6), end = '<=>')
    print(repr(x*x*x).rjust(10))

# demo subplot
np.random.seed(2019)
# normal distribution 
data = np.random.randn(2, 100)
print(data)
print(len(data[0]))
print(data[0])

# (sigma = 2.5^2, mu = 0)
data[1] = 10 * np.random.randn(100) + 0

print(len(data[0]))
print(data[0])

# create 4 figures
# figure size (x_size, y_size)
fig, axs = plt.subplots(2, 2, figsize = (10, 10))

# position of each figure
# x is rang y is precentage

axs[0, 0].hist(data[0], bins = 20)
axs[0, 1].hist(data[1])
axs[1, 0].scatter(data[0], data[1]*2, marker = "x")
axs[1, 1].hist2d(data[0], data[1], bins = 20)

plt.show()
