import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('stock_prices.csv')

scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

def create_dataset(data, time_steps):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:(i + time_steps)])
        y.append(data[i + time_steps])
    return np.array(X), np.array(y)

time_steps = 30
n_features = data_scaled.shape[1]

X_train, y_train = create_dataset(data_scaled, time_steps)
X_test, y_test = create_dataset(data_scaled, time_steps)

inputs = layers.Input(shape=(time_steps, n_features))
encoder = layers.LSTM(64, return_sequences=True)(inputs)
encoder = layers.Dropout(0.2)(encoder)
encoder = layers.LSTM(32, return_sequences=True)(encoder)
encoder = layers.Flatten()(encoder)
encoder = layers.Dense(16)(encoder)

decoder = layers.RepeatVector(1)(encoder)
decoder = layers.LSTM(32, return_sequences=True)(decoder)
decoder = layers.Dropout(0.2)(decoder)
decoder = layers.LSTM(64, return_sequences=True)(decoder)
output = layers.TimeDistributed(layers.Dense(n_features))(decoder)

model = Model(inputs=inputs, outputs=output)
model.compile(optimizer='adam', loss='mse')

model.fit(X_train, y_train, epochs=100, batch_size=32)

loss = model.evaluate(X_test, y_test)
print('Test Loss:', loss)

predictions = model.predict(X_test)

predictions_inv = scaler.inverse_transform(predictions)
y_test_inv = scaler.inverse_transform(y_test)

import matplotlib.pyplot as plt
plt.plot(predictions_inv[:,0], label='Predicted')
plt.plot(y_test_inv[:,0], label='True')
plt.legend()
plt.show()
