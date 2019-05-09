#!/usr/bin/python3
# import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# initialize figure and axes object
fig = plt.figure()
ax_1 = fig.add_subplot(2,1,1)
ax_2 = fig.add_subplot(2,1,2)
# load in data
file_dir = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
tips = pd.read_csv(file_dir)
print(tips)
print(len(tips))

# create a=violinplot
ax_1.violinplot(tips["total_bill"], vert = False)
ax_2.scatter(tips["total_bill"], tips["tip"])

# show the plot
plt.show()
