import pandas as pd
from io import StringIO
from sklearn import linear_model
import matplotlib.pyplot as plt

# read excel data
csv_data = 'square_feet,price\n15,645\n20,745\n25,845\n30,945\n35,1145\n40,1545\n60,1845\n'

# read inot pandas dataframe
df = pd.read_csv(StringIO(csv_data))

# linear regression
regr = linear_model.LinearRegression()
x = df['square_feet'].values.reshape(7,1)
y = df['price'].values.reshape(7,1)

# print(x.reshape(7,1), y.reshape(7,1))

regr.fit(x, y)
# print out parameters
print(f'coefficient: {regr.coef_}'+'\n')
print(f'intercept: {regr.intercept_}'+'\n')

# prediction data
y_1 = regr.predict(x)

plt.scatter(x, y, color='blue',label='exp')

plt.plot(x, y_1, color='red', linewidth=4,label='prediction')

plt.title('Liner')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.text(0,0,r'$\mu=100,\ \sigma=15$',style='italic', weight='bold', size='x-large')
plt.axis([0, 1.1*x.max(), 0, 1.1*y.max()])
plt.grid(True)

plt.show()
