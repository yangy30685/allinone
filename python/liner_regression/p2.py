import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
  
x = np.arange(10,dtype='float64').reshape((10,1))
y = x**1.3

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(x,y)

# Make predictions using the testing set
y_pred = regr.predict(x)

# The coefficients
print('Coefficients: \n', regr.coef_)
print('intercept: \n', regr.intercept_ )
  
# The mean squared error
print("Mean squared error: %.4f"% mean_squared_error(y,y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.4f' % r2_score(y, y_pred))

# Plot outputs
# marker=r'$\clubsuit$' alpha=1, marker='o',label="x_test"
plt.scatter(x, y, c="r",label="x_test")
plt.plot(x, y_pred, color='blue', linewidth=3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Liner')
plt.legend(loc='upper left')

plt.text(4, 0, r'$\mu=100,\ \sigma=15$')
plt.grid(True)

plt.show()