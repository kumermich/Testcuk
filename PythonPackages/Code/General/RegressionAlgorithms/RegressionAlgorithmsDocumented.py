"""! @brief Python program showcasing seven widely used Regresseion Algorithms."""
##
# @file RegressionAlgorithmsDocumented.py
#
# @brief This code file compares various regression models on the diabetes dataset using scikit-learn.

#######################
# Author: Sadegh Naderi
# Date created: 04.08.2023
# Path: BA23-14-Packages\report\Code\General\RegressionAlgorithms\RegressionAlgorithmsDocumented.py
# Version: 12
# Reviewed by: Sadegh Naderi
# Review Date: 08.08.2023
#######################


##
# @file RegressionAlgorithmsDocumented.py
#
# @section description_of_file Description
# The code demonstrates how to perform multiple feature regression, including linear, polynomial, ridge, lasso,
# elastic net, decision tree, and support vector regression, and evaluates their performance using R^2 and MSE scores.
#
# @section libraries Required Libraries
# The following code imports several libraries used in the script for various tasks:
# - numpy (as np): NumPy for numerical operations.
#   - For detailed documentation, visit: https://numpy.org/doc/
# - pandas (as pd): Pandas for data manipulation.
#   - For detailed documentation, visit: https://pandas.pydata.org/docs/
# - matplotlib.pyplot (as plt): Matplotlib for plotting.
#   - For detailed documentation, visit: https://matplotlib.org/stable/index.html
# - sklearn: Scikit-learn library for machine learning tasks, including regression models, feature engineering, and
# evaluation metrics.
#   - For detailed documentation, visit: https://scikit-learn.org/stable/
#
# @section authors Author
# - Created by Sadegh Naderi on 04.08.2023.
# - Modified by Sadegh Naderi on 04.08.2023.
#

# Importing required libraries
import numpy as np                                                             # NumPy for numerical operations
import pandas as pd                                                            # Pandas for data manipulation
import matplotlib.pyplot as plt                                                # Matplotlib for plotting
from sklearn.datasets import load_diabetes                                     # To load the Diabetes dataset
from sklearn.model_selection import train_test_split                           # To split data into training and testing sets
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet    # Regression models
from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler             # Feature engineering
from sklearn.tree import DecisionTreeRegressor                                 # Decision Tree Regressor
from sklearn.svm import SVR                                                    # Support Vector Regressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error                       # Evaluation metrics
from sklearn.tree import plot_tree                                             # For plotting the decision tree


# Load the diabetes dataset

## @var data
#  @brief The diabetes dataset.
#
#  This variable holds the diabetes dataset obtained by calling the `load_diabetes()` function from scikit-learn.
#  The diabetes dataset is a built-in dataset in scikit-learn, containing ten baseline variables and a quantitative
#  measure of disease progression one year after baseline for 442 diabetes patients.
#  For more details about the dataset, refer to the scikit-learn documentation.

data = load_diabetes()

# Create a pandas DataFrame from the dataset

## @var diabetes_df
#  @brief DataFrame representing the diabetes dataset.
#
#  This variable holds a pandas DataFrame created from the diabetes dataset obtained from the `data` variable.
#  The DataFrame contains the feature variables (baseline variables) as columns, and the target variable
#  'DiabetesProgression' as an additional column.
#
#  @note The feature variables are obtained from the `data.data` attribute, and the column names are set using the
#  `data.feature_names` attribute. The target variable is obtained from the `data.target` attribute.
#  The `head()` method is called on the DataFrame to display the first few rows.

diabetes_df = pd.DataFrame(data.data, columns=data.feature_names)
# Add the target variable 'target' to the DataFrame
diabetes_df['DiabetesProgression'] = data.target
# Display the DataFrame
print(diabetes_df.head())
print()

## @var X
#  @brief The feature data for regression.
#
#  This variable holds a single feature extracted from the `data.data` using slicing. In this case, it represents the
#  third feature (feature #2 (BMI)) from the dataset, used for single feature regression.
#
#  @note The feature data is expected to be a 1D array, but it will be reshaped to a 2D array before using it in
#  scikit-learn models.

## @var y
#  @brief The target variable data for regression.
#
#  This variable holds the target variable data from the `data.target` attribute. It represents the corresponding target
#  values for the single feature `X`.

# single feature regression (only for linear and polynomial algorithms)
X, y = data.data[:, 2], data.target  # Extract a single feature (feature #2) as X, and the target variable as y

# Reshape X from a 1D array to a 2D array (required by scikit-learn)
X = X.reshape(-1, 1)

## @var X_train
#  @brief The feature data for training.
#
#  This variable holds the feature data (X) for training the regression models.

## @var X_test
#  @brief The feature data for testing.
#
#  This variable holds the feature data (X) for testing the regression models.

## @var y_train
#  @brief The target variable for training.
#
#  This variable holds the target variable (y) for training the regression models.

## @var y_test
#  @brief The target variable for testing.
#
#  This variable holds the target variable (y) for testing the regression models.

## @var test_size
#  @brief The proportion of the dataset to include in the test split.
#
#  This variable holds the value representing the proportion of the dataset to be included in the test split.
#  The value is specified as a float between 0.0 and 1.0, where 0.2 means 20% of the dataset will be used for testing,
#  and the remaining 80% will be used for training.

## @var random_state
#  @brief The random seed for reproducibility of the split.
#
#  This variable holds the random seed used by the random number generator for shuffling the data before splitting.
#  It ensures that the same random split is generated each time the code is executed with the same value of
#  random_state.

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model

## @var model
#  @brief The linear regression model.
#
#  This variable holds an instance of the LinearRegression class from scikit-learn. It is used to perform linear
#  regression on the training data.
#
#  @note The model will be fit (trained) on the training data using the `fit` method.

model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test data

## @var y_pred
#  @brief Predicted target variable values.
#
#  This variable holds the predicted target variable values obtained by applying the trained linear regression model
#  (`model`) on the test data (`X_test`). The `predict` method of the model is used for making these predictions.

y_pred = model.predict(X_test)

# Plot the data and the linear regression line

## @var label
#  @brief This parameter provides a label to identify the data points in the scatter plot.
#
## @var marker
#  @brief The marker style for the data points.
#  This parameter specifies the marker style for the data points in the scatter plot.
#  For example, 'x' represents cross markers.
#
## @var color
#  @brief The color of the data points or line.
#  This parameter specifies the color of the data points in the scatter plot or the color of the linear
#  regression line.
#  For example, 'r' represents red color, and 'g' represents green color.

plt.scatter(X_train, y_train, label='Training data')  # Scatter plot for training data points
plt.scatter(X_test, y_test, label='Testing data', marker='x', color='r') # Scatter plot for testing data points with red 'x' markers
plt.plot(X_test, y_pred, color='g', label='Linear regression line')  # Plotting the linear regression line with green color
plt.xlabel('BMI')
plt.ylabel('Diabetes Progression')
plt.title('Linear Regression with one input variable')
plt.legend()
plt.grid(True)
plt.savefig('linearRegressionPlot.png')
plt.show()


# Create polynomial features of degree 4
## @var poly
#  @brief The polynomial feature transformer.
#  This variable holds an instance of the PolynomialFeatures class with the specified degree (4).
#  It is used to transform the input data into polynomial features.
poly = PolynomialFeatures(degree=4)

## @var X_train_poly
#  @brief The training data with polynomial features.
#  This variable holds the training data with polynomial features after fitting the PolynomialFeatures transformer.
X_train_poly = poly.fit_transform(X_train)

## @var X_test_poly
#  @brief The testing data with polynomial features.
#  This variable holds the testing data with polynomial features after transforming with the PolynomialFeatures transformer.
X_test_poly = poly.transform(X_test)

# Create and fit the linear regression model

## @var model
#  @brief The linear regression model.
#  This variable holds an instance of the LinearRegression class after fitting with the training data with polynomial features.
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Make predictions on the test data

## @var y_pred
#  @brief The predicted values on the test data.
#  This variable holds the predicted target values produced by the linear regression model (model)
#  using the polynomial features (X_test_poly) as input data.
y_pred = model.predict(X_test_poly)

# Sort the data and predictions based on X for a smooth plot

## @var sort_indices
#  @brief The indices for sorting the testing data and predictions.
#  This variable holds an array of indices that can be used to sort the testing data (X_test)
#  and the corresponding predicted values (y_pred) based on the values of X_test for a smooth plot.
sort_indices = np.argsort(X_test.flatten())

## @var X_test_sorted
#  @brief The sorted testing data for a smooth plot.
#  This variable holds the testing data sorted based on the values of X for visualization purposes.
X_test_sorted = X_test[sort_indices]

## @var y_pred_sorted
#  @brief The sorted predictions for a smooth plot.
#  This variable holds the predicted values sorted based on the values of X_test_sorted for visualization purposes.
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


# multiple feature regression
X, y = data.data, data.target

# Split the data into training and test sets (80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## @var linear_model
#  @brief The linear regression model.
#
#  This variable holds the linear regression model, which will be used for prediction.

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

## @var y_train_pred_linear
#  @brief The predicted target values on training data (linear regression).
#
#  This variable holds the predicted target values for the training data using the linear regression model.

## @var y_test_pred_linear
#  @brief The predicted target values on test data (linear regression).
#
#  This variable holds the predicted target values for the test data using the linear regression model.

# Predict on training and test data
y_train_pred_linear = linear_model.predict(X_train)
y_test_pred_linear = linear_model.predict(X_test)

## @var r2_train_linear
#  @brief The R^2 score on training data (linear regression).
#
#  This variable holds the R^2 score for the training data using the linear regression model.

## @var r2_test_linear
#  @brief The R^2 score on test data (linear regression).
#
#  This variable holds the R^2 score for the test data using the linear regression model.

# Calculate R^2 scores for train and test
r2_train_linear = r2_score(y_train, y_train_pred_linear)
r2_test_linear = r2_score(y_test, y_test_pred_linear)

## @var mse_train_linear
#  @brief The mean squared error (MSE) on training data (linear regression).
#
#  This variable holds the mean squared error (MSE) for the training data using the linear regression model.

## @var mse_test_linear
#  @brief The mean squared error (MSE) on test data (linear regression).
#
#  This variable holds the mean squared error (MSE) for the test data using the linear regression model.

# Calculate MSE scores for train and test
mse_train_linear = mean_squared_error(y_train, y_train_pred_linear)
mse_test_linear = mean_squared_error(y_test, y_test_pred_linear)

## @var degree
#  @brief The degree of the polynomial regression function.

## @var poly_features
#  @brief The polynomial feature transformer.
#
#  This variable holds the polynomial feature transformer with the specified degree.

# Polynomial Regression (degree=4)
degree = 4
poly_features = PolynomialFeatures(degree=degree)
X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)

## @var poly_model
#  @brief The polynomial regression model.
#
#  This variable holds the polynomial regression model, which will be used for prediction.

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

## @var y_train_pred_poly
#  @brief The predicted target values on training data (polynomial regression).
#
#  This variable holds the predicted target values for the training data using the polynomial regression model.

## @var y_test_pred_poly
#  @brief The predicted target values on test data (polynomial regression).
#
#  This variable holds the predicted target values for the test data using the polynomial regression model.

# Predict on training and test data
y_train_pred_poly = poly_model.predict(X_train_poly)
y_test_pred_poly = poly_model.predict(X_test_poly)

## @var r2_train_poly
#  @brief The R^2 score on training data (polynomial regression).
#
#  This variable holds the R^2 score for the training data using the polynomial regression model.

## @var r2_test_poly
#  @brief The R^2 score on test data (polynomial regression).
#
#  This variable holds the R^2 score for the test data using the polynomial regression model.

# Calculate R^2 scores for train and test
r2_train_poly = r2_score(y_train, y_train_pred_poly)
r2_test_poly = r2_score(y_test, y_test_pred_poly)

## @var mse_train_poly
#  @brief The mean squared error (MSE) on training data (polynomial regression).
#
#  This variable holds the mean squared error (MSE) for the training data using the polynomial regression model.

## @var mse_test_poly
#  @brief The mean squared error (MSE) on test data (polynomial regression).
#
#  This variable holds the mean squared error (MSE) for the test data using the polynomial regression model.

# Calculate MSE scores for train and test
mse_train_poly = mean_squared_error(y_train, y_train_pred_poly)
mse_test_poly = mean_squared_error(y_test, y_test_pred_poly)


# Ridge Regression

## @var scaler
#  @brief The Min-Max Scaler.
#  This variable holds an instance of the MinMaxScaler class used for scaling the input data.
#
## @var X_train_scaled
#  @brief The scaled training data.
#  This variable holds the training data (X_train) after being scaled using Min-Max scaling.
#  Min-Max scaling transforms the data to the range [0, 1] to improve the performance of the Ridge Regression model.
#
## @var X_test_scaled
#  @brief The scaled testing data.
#  This variable holds the testing data (X_test) after being scaled using Min-Max scaling.
#  The scaling is done based on the parameters computed from the training data to ensure consistency.

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


## @var ridge_model
#  @brief The ridge regression model.
#
#  This variable holds the ridge regression model, which will be used for prediction.

ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train_scaled, y_train)

## @var y_train_pred_ridge
#  @brief The predicted target values on training data (ridge regression).
#
#  This variable holds the predicted target values for the training data using the ridge regression model.

## @var y_test_pred_ridge
#  @brief The predicted target values on test data (ridge regression).
#
#  This variable holds the predicted target values for the test data using the ridge regression model.

# Predict on training and test data
y_train_pred_ridge = ridge_model.predict(X_train_scaled)
y_test_pred_ridge = ridge_model.predict(X_test_scaled)

## @var r2_train_ridge
#  @brief The R^2 score on training data (ridge regression).
#
#  This variable holds the R^2 score for the training data using the ridge regression model.

## @var r2_test_ridge
#  @brief The R^2 score on test data (ridge regression).
#
#  This variable holds the R^2 score for the test data using the ridge regression model.

# Calculate R^2 scores for train and test
r2_train_ridge = r2_score(y_train, y_train_pred_ridge)
r2_test_ridge = r2_score(y_test, y_test_pred_ridge)

## @var mse_train_ridge
#  @brief The mean squared error (MSE) on training data (ridge regression).
#
#  This variable holds the mean squared error (MSE) for the training data using the ridge regression model.

## @var mse_test_ridge
#  @brief The mean squared error (MSE) on test data (ridge regression).
#
#  This variable holds the mean squared error (MSE) for the test data using the ridge regression model.

# Calculate MSE scores for train and test
mse_train_ridge = mean_squared_error(y_train, y_train_pred_ridge)
mse_test_ridge = mean_squared_error(y_test, y_test_pred_ridge)


print('ridge regression linear model coeff:\n{}'
      .format(ridge_model.coef_))

## @var alpha_values
#  @brief The alpha values for ridge and lasso regression.
#
#  This variable holds the array of 100 alpha values from 10^-4 to 10^2 used for plotting.

## @var coefficients
#  @brief The coefficients for ridge regression.
#
#  This variable holds a list to store the coefficients for each alpha used for plotting.

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

## @var figsize
#  @brief Tuple (width, height) in inches, defining the size of the figure.
#
#  This variable defines the size of the figure in inches. The width and height of the figure are specified as a tuple.
#  For example, `figsize=(10, 6)` will create a figure with a width of 10 inches and a height of 6 inches.

## @var dpi
#  @brief The resolution (dots per inch) for saving the figure to a file.
#
#  This variable sets the resolution of the saved figure in dots per inch (DPI). A higher DPI results in a higher-quality
#  image, but also increases the file size. For example, `dpi=300` will save the figure with a resolution of 300 DPI.

## @var bbox_inches
#  @brief The portion of the figure to save (tight, 'standard', 'None', or a Bbox object).
#
#  This variable specifies which portion of the figure to save when calling `plt.savefig()`. The options include:
#  - 'tight': Crop the figure to remove any white space around the plot elements.
#  - 'standard': Save the full figure with all elements, including any white space.
#  - 'None': Save the full figure with all elements, including any white space.
#  - A Bbox object: Allows specifying a custom bounding box to save a specific portion of the figure.

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


## @var lasso_model
#  @brief The lasso regression model.
#
#  This variable holds the lasso regression model, which will be used for prediction.

# Lasso Regression
lasso_model = Lasso(alpha=1.0)
lasso_model.fit(X_train_scaled, y_train)

## @var y_train_pred_lasso
#  @brief The predicted target values on training data (lasso regression).
#
#  This variable holds the predicted target values for the training data using the lasso regression model.

## @var y_test_pred_lasso
#  @brief The predicted target values on test data (lasso regression).
#
#  This variable holds the predicted target values for the test data using the lasso regression model.

# Predict on training and test data
y_train_pred_lasso = lasso_model.predict(X_train_scaled)
y_test_pred_lasso = lasso_model.predict(X_test_scaled)

## @var r2_train_lasso
#  @brief The R^2 score on training data (lasso regression).
#
#  This variable holds the R^2 score for the training data using the lasso regression model.

## @var r2_test_lasso
#  @brief The R^2 score on test data (lasso regression).
#
#  This variable holds the R^2 score for the test data using the lasso regression model.

# Calculate R^2 scores for train and test
r2_train_lasso = r2_score(y_train, y_train_pred_lasso)
r2_test_lasso = r2_score(y_test, y_test_pred_lasso)

## @var mse_train_lasso
#  @brief The mean squared error (MSE) on training data (lasso regression).
#
#  This variable holds the mean squared error (MSE) for the training data using the lasso regression model.

## @var mse_test_lasso
#  @brief The mean squared error (MSE) on test data (lasso regression).
#
#  This variable holds the mean squared error (MSE) for the test data using the lasso regression model.

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


## @var elastic_net_model
#  @brief The elastic net regression model.
#
#  This variable holds the elastic net regression model, which will be used for prediction.

# Elastic Net Regression
elastic_net_model = ElasticNet(alpha=1.0, l1_ratio=0.5)
elastic_net_model.fit(X_train_scaled, y_train)

## @var y_train_pred_enet
#  @brief The predicted target values on training data (elastic net regression).
#
#  This variable holds the predicted target values for the training data using the elastic net regression model.

## @var y_test_pred_enet
#  @brief The predicted target values on test data (elastic net regression).
#
#  This variable holds the predicted target values for the test data using the elastic net regression model.

# Predict on training and test data
y_train_pred_enet = elastic_net_model.predict(X_train_scaled)
y_test_pred_enet = elastic_net_model.predict(X_test_scaled)

## @var r2_train_enet
#  @brief The R^2 score on training data (elastic net regression).
#
#  This variable holds the R^2 score for the training data using the elastic net regression model.

## @var r2_test_enet
#  @brief The R^2 score on test data (elastic net regression).
#
#  This variable holds the R^2 score for the test data using the elastic net regression model.

# Calculate R^2 scores for train and test
r2_train_enet = r2_score(y_train, y_train_pred_enet)
r2_test_enet = r2_score(y_test, y_test_pred_enet)

## @var mse_train_enet
#  @brief The mean squared error (MSE) on training data (elastic net regression).
#
#  This variable holds the mean squared error (MSE) for the training data using the elastic net regression model.

## @var mse_test_enet
#  @brief The mean squared error (MSE) on test data (elastic net regression).
#
#  This variable holds the mean squared error (MSE) for the test data using the elastic net regression model.

# Calculate MSE scores for train and test
mse_train_enet = mean_squared_error(y_train, y_train_pred_enet)
mse_test_enet = mean_squared_error(y_test, y_test_pred_enet)
print('Elastic Net regression linear model coeff:\n{}'
      .format(elastic_net_model.coef_))

## @var decision_tree_model
#  @brief The decision tree regression model.
#
#  This variable holds the decision tree regression model, which will be used for prediction.

# Decision Tree Regression
decision_tree_model = DecisionTreeRegressor(random_state=42)
decision_tree_model.fit(X_train, y_train)

## @var y_train_pred_dt
#  @brief The predicted target values on training data (decision tree regression).
#
#  This variable holds the predicted target values for the training data using the decision tree regression model.

## @var y_test_pred_dt
#  @brief The predicted target values on test data (decision tree regression).
#
#  This variable holds the predicted target values for the test data using the decision tree regression model.

# Predict on training and test data
y_train_pred_dt = decision_tree_model.predict(X_train)
y_test_pred_dt = decision_tree_model.predict(X_test)

## @var r2_train_dt
#  @brief The R^2 score on training data (decision tree regression).
#
#  This variable holds the R^2 score for the training data using the decision tree regression model.

## @var r2_test_dt
#  @brief The R^2 score on test data (decision tree regression).
#
#  This variable holds the R^2 score for the test data using the decision tree regression model.

# Calculate R^2 scores for train and test
r2_train_dt = r2_score(y_train, y_train_pred_dt)
r2_test_dt = r2_score(y_test, y_test_pred_dt)

## @var mse_train_dt
#  @brief The mean squared error (MSE) on training data (decision tree regression).
#
#  This variable holds the mean squared error (MSE) for the training data using the decision tree regression model.

## @var mse_test_dt
#  @brief The mean squared error (MSE) on test data (decision tree regression).
#
#  This variable holds the mean squared error (MSE) for the test data using the decision tree regression model.

# Calculate MSE scores for train and test
mse_train_dt = mean_squared_error(y_train, y_train_pred_dt)
mse_test_dt = mean_squared_error(y_test, y_test_pred_dt)

## @var svr_model
#  @brief The support vector regression model.
#
#  This variable holds the support vector regression model, which will be used for prediction.

# Plot the Decision Tree with max_depth=2

## @var feature_names
#  @brief List of column names used for labeling the features in the decision tree plot.

## @var filled
#  @brief If True, fill the nodes with colors indicating the majority class.

## @var rounded
#  @brief If True, display the nodes as rounded rectangles.

## @var max_depth
#  @brief Maximum depth of the decision tree to plot.

## @var fontsize
#  @brief Font size for the text in the decision tree plot.

plt.figure(figsize=(12, 12))
plot_tree(decision_tree_model, feature_names=data.feature_names, filled=False, rounded=True, max_depth=2, fontsize=11)
plt.title("Decision Tree Regression (Max Depth = 2)", fontsize=16)
plt.savefig('decisionTreePlot.png')
plt.show()

# plotting the feature importance

## @var feature_importance
#  @brief The feature importance scores obtained from the decision tree model.
#
#  This variable holds the feature importance scores obtained from the decision tree regression model.

## @var sorted_idx
#  @brief The sorted indices of features based on their importance scores.
#
#  This variable holds the sorted indices of features in ascending order of their importance scores.

## @var feature_names
#  @brief The names of features arranged in ascending order of importance.
#
#  This variable holds the names of features arranged in ascending order of their importance scores.

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


# Support Vector Regression (SVR)
# Create a pipeline with StandardScaler and SVR
svr_model = make_pipeline(StandardScaler(), SVR(kernel='rbf'))
# Fit the SVR model using the pipeline
svr_model.fit(X_train, y_train)

## @var y_train_pred_svr
#  @brief The predicted target values on training data (support vector regression).
#
#  This variable holds the predicted target values for the training data using the support vector regression model.

## @var y_test_pred_svr
#  @brief The predicted target values on test data (support vector regression).
#
#  This variable holds the predicted target values for the test data using the support vector regression model.

# Predict on training and test data
y_train_pred_svr = svr_model.predict(X_train)
y_test_pred_svr = svr_model.predict(X_test)

## @var r2_train_svr
#  @brief The R^2 score on training data (support vector regression).
#
#  This variable holds the R^2 score for the training data using the support vector regression model.

## @var r2_test_svr
#  @brief The R^2 score on test data (support vector regression).
#
#  This variable holds the R^2 score for the test data using the support vector regression model.

# Calculate R^2 scores for train and test
r2_train_svr = r2_score(y_train, y_train_pred_svr)
r2_test_svr = r2_score(y_test, y_test_pred_svr)

## @var mse_train_svr
#  @brief The mean squared error (MSE) on training data (support vector regression).
#
#  This variable holds the mean squared error (MSE) for the training data using the support vector regression model.

## @var mse_test_svr
#  @brief The mean squared error (MSE) on test data (support vector regression).
#
#  This variable holds the mean squared error (MSE) for the test data using the support vector regression model.

# Calculate MSE scores for train and test
mse_train_svr = mean_squared_error(y_train, y_train_pred_svr)
mse_test_svr = mean_squared_error(y_test, y_test_pred_svr)


## @var results_dict
#  @brief The dictionary to store the regression model results.
#
#  This variable holds a dictionary to store the R^2 and MSE scores for each regression model.

## @var results_df
#  @brief The DataFrame to store the regression model results.
#
#  This variable holds a DataFrame to store the R^2 and MSE scores for each regression model.

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

## @var results_df
#  @brief The DataFrame to store the regression model results.
#
#  This variable holds a DataFrame to store the R^2 and MSE scores for each regression model.

# Create the DataFrame
results_df = pd.DataFrame(results_dict)

# Display the DataFrame
print(results_df)
