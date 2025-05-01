#######################
# Author: Sadegh Naderi
# Date created: 2023-08-12
# Path: PythonPackages/report/Code/General/TimeSeries/TimeSeriesForecasting.py
# Version: 1
# Reviewed by: Sadegh Naderi
# Review Date: 2023-08-13
#######################


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate a synthetic time series dataset
np.random.seed(42)
time = pd.date_range(start='2023-01-01', periods=100, freq='D')
values = np.sin(np.arange(0, 2 * np.pi, 2 * np.pi / 100)) + np.random.normal(0, 0.2, 100)
df = pd.DataFrame({'Time': time, 'Value': values})
df.set_index('Time', inplace=True)

# Create lag features
for i in range(1, 6):
    df[f'Lag_{i}'] = df['Value'].shift(i)

# Drop rows with missing values due to lag
df.dropna(inplace=True)

# Split the data into training and testing sets
X = df.drop('Value', axis=1)
y = df['Value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Plot the original data and predictions
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], label='Original Data')
plt.plot(X_test.index, y_pred, label='Predictions', linestyle='dashed')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Time Series Forecasting with Linear Regression')
plt.savefig('timeSeriesForecast.png')
plt.show()

