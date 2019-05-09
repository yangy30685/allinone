import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

# read data from csv online        
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv" 
df = pd.read_csv(data_url)

# describe the data information
print (df.describe())

# count function
count_1 = df['sex'].value_counts()
count_2 = df['day'].value_counts()

print (count_1, count_2)
print ('+'*50)

# screen the data with conditions
print(df[(df.tip > 7) | (df.total_bill > 50)])
print ('+'*50)

# transform x to y by T 
print (df.T)
print ('~'*50)

# sort the values by tips ascending
new_df = df.sort_values(by = 'tip')
print(new_df[(new_df.tip <= 3)])

# group the data
group = df.groupby('day')
print(group.first())
print ('-'*50)

# create a random data 6 rows and 4 columns
czf_data = pd.DataFrame(np.random.randn(6,4), columns = ['a','b','c','d'])
czf_data = czf_data * 100
print(czf_data)
print ('#'*50)

# change data type to int
czf_data = czf_data.astype('int')

# loc is label for row change to not a number
czf_data.loc[2,:] = np.nan
print(czf_data)
print ('='*50)