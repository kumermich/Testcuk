##
# @file: TimeSeriesForecastingDocumented.py
#
# @brief This code file demonstrates time series forecasting using linear regression.

############################
# Author: Sadegh Naderi
# Date created: 12.08.2023
# Path: PythonPackages/report/Code/General/TimeSeries/TimeSeriesForecastingDocumented.py
# Version: 2.0
# Reviewed by: Sadegh Naderi
# Review Date: 02.09.2023
############################


##
# @file: TimeSeriesForecastingDocumented.py
#
# @section description_of_file Description
# This code generates a synthetic time series dataset and performs time series forecasting using a linear regression
# model. Lag features are created to predict the current day's value based on past values, and the model's predictions
# are plotted alongside the original data.
#
# @section libraries Required Libraries
# The following code imports several libraries used in the script for various tasks:
# - numpy (as np): NumPy for numerical operations.
#   - For detailed documentation, visit: https://numpy.org/doc/
# - pandas (as pd): Pandas for data manipulation.
#   - For detailed documentation, visit: https://pandas.pydata.org/docs/
# - sklearn.model_selection: Scikit-learn's train_test_split for splitting the dataset.
#   - For detailed documentation, visit: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
# - sklearn.linear_model: Scikit-learn's LinearRegression for linear regression modeling.
#   - For detailed documentation, visit: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
# - matplotlib.pyplot (as plt): Matplotlib for plotting.
#   - For detailed documentation, visit: https://matplotlib.org/stable/index.html
#
# @section authors Author
# - Created by Sadegh Naderi on 12.08.2023.
# - Modified by Sadegh Naderi on 02.09.2023.
#

## @var time
#  @brief An array containing date-time values representing the time index.
#
#  The time index for the time series data.

## @var values
#  @brief An array containing the synthetic time series values.
#
#  The synthetic time series values generated using sine function and noise.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate synthetic time series data
np.random.seed(42)
time = pd.date_range(start='2023-01-01', periods=100, freq='D')
values = np.sin(np.arange(0, 2 * np.pi, 2 * np.pi / 100)) + np.random.normal(0, 0.2, 100)
df = pd.DataFrame({'Time': time, 'Value': values})
df.set_index('Time', inplace=True)

## @var lag_columns
#  @brief A list containing the names of lag feature columns.
#
#  The names of the lag feature columns created in the DataFrame.

# Create lag features
for i in range(1, 6):
    df[f'Lag_{i}'] = df['Value'].shift(i)

# Drop rows with missing values due to lag
df.dropna(inplace=True)

## @var X
#  @brief The feature matrix for training the linear regression model.
#
#  The feature matrix containing lag values for training the model.

## @var y
#  @brief The target vector for training the linear regression model.
#
#  The target vector containing the corresponding actual values for training the model.

# Split the data into training and testing sets

## @var X_train
# @brief Training features.
#
# This variable holds the training features (input variables) for the linear regression model.

## @var X_test
# @brief Testing features.
#
# This variable holds the testing features (input variables) for the linear regression model.

## @var y_train
# @brief Training labels.
#
# This variable holds the training labels (output variables) corresponding to the training features.

## @var y_test
# @brief Testing labels.
#
# This variable holds the testing labels (output variables) corresponding to the testing features.

## @var test_size
# @brief Test set size.
#
# This parameter specifies the proportion of the dataset that will be used for testing.
# The value is set as a fraction (e.g., 0.2 for 20% of the data) in the call to train_test_split.

## @var shuffle
# @brief Shuffle parameter.
#
# This parameter controls whether the dataset is shuffled before splitting into training and testing sets.
# When set to True, the data points are randomly shuffled before the split.
# When set to False, the data points are selected in order (e.g., for time series data).

X = df.drop('Value', axis=1)
y = df['Value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

## @var model
#  @brief The linear regression model trained on the training data.
#
#  The linear regression model used for making predictions.

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set

## @var y_pred
# @brief Predicted values.
#
# This variable holds the predicted values generated by the trained linear regression model
# for the testing set features (X_test).

y_pred = model.predict(X_test)

# Plot the original data and predictions

## @var figsize
# @brief Figure size for plotting.
#
# This variable determines the dimensions (width and height) of the figure used for plotting.

## @var label
# @brief Label for the plot.
#
# This variable specifies the label to be used for different plotted elements (e.g., lines).

## @var index
# @brief Index column.
#
# This variable holds the values that will be used as the index column when setting the DataFrame index.

## @var linestyle
# @brief Line style for plotting.
#
# This variable specifies the style of the line used for plotting (e.g., solid, dashed).

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], label='Original Data')
plt.plot(X_test.index, y_pred, label='Predictions', linestyle='dashed')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Time Series Forecasting with Linear Regression')

## @var plot_filename
#  @brief The filename for saving the plot image.
#
#  The filename used to save the generated plot image.

# Save the figure
plot_filename = 'time_series_forecast.png'
plt.savefig(plot_filename)

# Display the figure
plt.show()
