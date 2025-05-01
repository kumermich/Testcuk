#######################
# Author: Sadegh Naderi
# Date created: 09.08.2023
# Path: BA23-14-Packages\report\Code\General\RegressionAlgorithms\RegressionAlgorithms.py
# Version: 3.0
# Reviewed by: Sadegh Naderi
# Review Date: 25.08.2023
#######################


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.datasets import load_diabetes 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet 
from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR 
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.tree import plot_tree

# Load the diabetes dataset
data = load_diabetes()
# Create a pandas DataFrame from the dataset
diabetes_df = pd.DataFrame(data.data, columns=data.feature_names)
# Add the target variable 'target' to the DataFrame
diabetes_df['DiabetesProgression'] = data.target
# Display the DataFrame
print(diabetes_df.head())
# single feature regression (only for linear and polynomial algorithms)
X, y = data.data[:, 2], data.target  # Extract a single feature (feature #2) as X, and the target variable as y

# Reshape X from a 1D array to a 2D array (required by scikit-learn)
X = X.reshape(-1, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Plot the data and the linear regression line
plt.scatter(X_train, y_train, label='Training data')  # Scatter plot for training data points
plt.scatter(X_test, y_test, label='Testing data', marker='x', color='r') # Scatter plot for testing data points with red 'x' markers
plt.plot(X_test, y_pred, color='g', label='Linear regression line')  # Plotting the linear regression line with green color
plt.xlabel('BMI')
plt.ylabel('Diabetes Progression')
plt.title('Linear Regression with one input variable')
plt.legend()
plt.grid(True)
#plt.savefig('linearRegressionPlot.png')
plt.show()

# Create polynomial features of degree 4
poly = PolynomialFeatures(degree=4)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test_poly)

# Sort the data and predictions based on X for a smooth plot
sort_indices = np.argsort(X_test.flatten())
X_test_sorted = X_test[sort_indices]
y_pred_sorted = y_pred[sort_indices]

# Plot the data and the polynomial regression line
plt.scatter(X_train, y_train, label='Training data')
plt.scatter(X_test, y_test, label='Testing data', marker='x', color='r')
plt.plot(X_test_sorted, y_pred_sorted, color='g', label='Polynomial regression line')
plt.xlabel('BMI')
plt.ylabel('Diabetes Progression')
plt.title('Polynomial Regression of degree 4 with one input variable')
plt.legend()
plt.grid(True)
plt.savefig('polynomialRegressionPlot.png')
plt.show()

# Load the diabetes dataset
data = load_diabetes()

# multiple feature regression
X, y = data.data, data.target

# Split the data into training and test sets (80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Predict on training and test data
y_train_pred_linear = linear_model.predict(X_train)
y_test_pred_linear = linear_model.predict(X_test)

# Calculate R^2 scores for train and test
r2_train_linear = r2_score(y_train, y_train_pred_linear)
r2_test_linear = r2_score(y_test, y_test_pred_linear)

# Calculate MSE scores for train and test
mse_train_linear = mean_squared_error(y_train, y_train_pred_linear)
mse_test_linear = mean_squared_error(y_test, y_test_pred_linear)


# Polynomial Regression (degree=4)
degree = 4
poly_features = PolynomialFeatures(degree=degree)
X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

# Predict on training and test data
y_train_pred_poly = poly_model.predict(X_train_poly)
y_test_pred_poly = poly_model.predict(X_test_poly)

# Calculate R^2 scores for train and test
r2_train_poly = r2_score(y_train, y_train_pred_poly)
r2_test_poly = r2_score(y_test, y_test_pred_poly)

# Calculate MSE scores for train and test
mse_train_poly = mean_squared_error(y_train, y_train_pred_poly)
mse_test_poly = mean_squared_error(y_test, y_test_pred_poly)


# Ridge Regression
# MinMax scaling
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train_scaled, y_train)

# Predict on training and test data
y_train_pred_ridge = ridge_model.predict(X_train_scaled)
y_test_pred_ridge = ridge_model.predict(X_test_scaled)

# Calculate R^2 scores for train and test
r2_train_ridge = r2_score(y_train, y_train_pred_ridge)
r2_test_ridge = r2_score(y_test, y_test_pred_ridge)

# Calculate MSE scores for train and test
mse_train_ridge = mean_squared_error(y_train, y_train_pred_ridge)
mse_test_ridge = mean_squared_error(y_test, y_test_pred_ridge)


print('ridge regression linear model coeff:\n{}'
      .format(ridge_model.coef_))

# plot the figure of the ridge regression coefficients with respect to different values of alpha
# Vary the alpha values
alpha_values = np.logspace(-4, 2, 100)  # 100 alpha values from 10^-4 to 10^2

coefficients = []  # List to store the coefficients for each alpha

for alpha in alpha_values:
    # Perform Ridge regression with current alpha
    ridge_model = Ridge(alpha=alpha)
    ridge_model.fit(X_train_scaled, y_train)
    coefficients.append(ridge_model.coef_)


# Plot the coefficients for each alpha
plt.figure(figsize=(10, 6))
for i in range(X.shape[1]):
    plt.plot(alpha_values, [coef[i] for coef in coefficients], label=f'Feature {i+1}')

plt.xscale('log')
plt.xlabel('Alpha')
plt.ylabel('Coefficient Value')
plt.title('Ridge Regression Coefficient curves')
plt.legend()
plt.grid(True)
plt.savefig('ridgeCoefficientsvsAlphaPlot.png', dpi=300, bbox_inches='tight')
plt.show()

# Lasso Regression
lasso_model = Lasso(alpha=1.0)
lasso_model.fit(X_train_scaled, y_train)

# Predict on training and test data
y_train_pred_lasso = lasso_model.predict(X_train_scaled)
y_test_pred_lasso = lasso_model.predict(X_test_scaled)

# Calculate R^2 scores for train and test
r2_train_lasso = r2_score(y_train, y_train_pred_lasso)
r2_test_lasso = r2_score(y_test, y_test_pred_lasso)

# Calculate MSE scores for train and test
mse_train_lasso = mean_squared_error(y_train, y_train_pred_lasso)
mse_test_lasso = mean_squared_error(y_test, y_test_pred_lasso)

print('lasso regression linear model coeff:\n{}'
      .format(lasso_model.coef_))

# plot the figure of the lasso regression coefficients with respect to different values of alpha
# Vary the alpha values
coefficients = []  # List to store the coefficients for each alpha

for alpha in alpha_values:
    # Perform Lasso regression with current alpha
    lasso_model = Lasso(alpha=alpha)
    lasso_model.fit(X_train_scaled, y_train)
    coefficients.append(lasso_model.coef_)

# Plot the coefficients for each alpha
plt.figure(figsize=(10, 6))
for i in range(X.shape[1]):
    plt.plot(alpha_values, [coef[i] for coef in coefficients], label=f'Feature {i+1}')

plt.xscale('log')
plt.xlabel('Alpha')
plt.ylabel('Coefficient Value')
plt.title('Lasso Regression Coefficient curves')
plt.legend()
plt.grid(True)
plt.savefig('lassoCoefficientsvsAlphaPlot.png', dpi=300, bbox_inches='tight')
plt.show()


# Elastic Net Regression
elastic_net_model = ElasticNet(alpha=1.0, l1_ratio=0.5)
elastic_net_model.fit(X_train_scaled, y_train)

# Predict on training and test data
y_train_pred_enet = elastic_net_model.predict(X_train_scaled)
y_test_pred_enet = elastic_net_model.predict(X_test_scaled)

# Calculate R^2 scores for train and test
r2_train_enet = r2_score(y_train, y_train_pred_enet)
r2_test_enet = r2_score(y_test, y_test_pred_enet)

# Calculate MSE scores for train and test
mse_train_enet = mean_squared_error(y_train, y_train_pred_enet)
mse_test_enet = mean_squared_error(y_test, y_test_pred_enet)


# Decision Tree Regression
decision_tree_model = DecisionTreeRegressor(random_state=42)
decision_tree_model.fit(X_train, y_train)

# Predict on training and test data
y_train_pred_dt = decision_tree_model.predict(X_train)
y_test_pred_dt = decision_tree_model.predict(X_test)

# Calculate R^2 scores for train and test
r2_train_dt = r2_score(y_train, y_train_pred_dt)
r2_test_dt = r2_score(y_test, y_test_pred_dt)

# Calculate MSE scores for train and test
mse_train_dt = mean_squared_error(y_train, y_train_pred_dt)
mse_test_dt = mean_squared_error(y_test, y_test_pred_dt)
# Support Vector Regression (SVR)
# Create a pipeline with StandardScaler and SVR
svr_model = make_pipeline(StandardScaler(), SVR(kernel='rbf'))
# Fit the SVR model using the pipeline
svr_model.fit(X_train, y_train)
# Predict on training and test data
y_train_pred_svr = svr_model.predict(X_train)
y_test_pred_svr = svr_model.predict(X_test)

# Calculate R^2 scores for train and test
r2_train_svr = r2_score(y_train, y_train_pred_svr)
r2_test_svr = r2_score(y_test, y_test_pred_svr)

# Calculate MSE scores for train and test
mse_train_svr = mean_squared_error(y_train, y_train_pred_svr)
mse_test_svr = mean_squared_error(y_test, y_test_pred_svr)


# Plot the Decision Tree with max_depth=2
plt.figure(figsize=(12, 12))
plot_tree(decision_tree_model, feature_names=data.feature_names, filled=False, rounded=True, max_depth=2, fontsize=11)
plt.title("Decision Tree Regression (Max Depth = 2)", fontsize=16)
plt.savefig('decisionTreePlot.png')
plt.show()

# plotting the feature importance
# Get the feature importance scores
feature_importance = decision_tree_model.feature_importances_
# Sort features by importance in ascending order
sorted_idx = np.argsort(feature_importance)
# Arrange feature names in ascending order of importance
feature_names = [data.feature_names[i] for i in sorted_idx]
# Plot the feature importance
plt.figure(figsize=(10, 6))
plt.barh(range(len(feature_importance)), feature_importance[sorted_idx], align='center')
plt.yticks(range(len(feature_importance)), feature_names)
plt.xlabel('Feature Importance')
plt.ylabel('Feature')
plt.title('Decision Tree Regression - Feature Importance')
plt.savefig('featureImportancePlot.png')
plt.show()

# saving all the r^2 and MSE scores in one dataframe
# Create a dictionary to store the results
results_dict = {
    'Model': ['Linear Regression', f'Polynomial Regression (degree={degree})', 'Ridge Regression', 'Lasso Regression',
              'Elastic Net Regression', 'Decision Tree Regression', 'Support Vector Regression'],
    'R^2 (Train)': [r2_train_linear, r2_train_poly, r2_train_ridge, r2_train_lasso, r2_train_enet, r2_train_dt,
                    r2_train_svr],
    'R^2 (Test)': [r2_test_linear, r2_test_poly, r2_test_ridge, r2_test_lasso, r2_test_enet, r2_test_dt, r2_test_svr],
    'MSE (Train)': [mse_train_linear, mse_train_poly, mse_train_ridge, mse_train_lasso, mse_train_enet, mse_train_dt,
                    mse_train_svr],
    'MSE (Test)': [mse_test_linear, mse_test_poly, mse_test_ridge, mse_test_lasso, mse_test_enet, mse_test_dt,
                   mse_test_svr]
}

# Create the DataFrame
results_df = pd.DataFrame(results_dict)

# Display the DataFrame
print(results_df)

