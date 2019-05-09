#!/usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
sns.set_context('paper')

tips = sns.load_dataset('tips')

# separate smoker by day 
sns.lmplot(x = 'tip', y= 'total_bill', col = 'day', data = tips)

plt.show()
