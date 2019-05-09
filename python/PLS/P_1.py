from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import mean_squared_error, r2_score
 
# Define PLS object
pls = PLSRegression(n_components=5)
 
# Fit
pls.fit(X_calib, Y_calib)
 
# Prediction
Y_pred = pls.predict(X_valid)
 
# Calculate scores
score = r2_score(Y_valid, Y_pred)
mse = mean_squared_error(Y_valid, Y_pred)