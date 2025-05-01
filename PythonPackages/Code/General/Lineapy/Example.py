############################
# Author: Sandesh Nonavinakere Sunil
# Date created: 29.01.2025
# Path: ML24-PythonPackages\Code\General\Lineapy\Example.py
# Version: 1.0
# Reviewed by: Sandesh Nonavinakere Sunil
# Review Date: 29.01.2025
############################

##
# @mainpage Model Training and Artifact Storage
#
# This project demonstrates the usage of TensorFlow to train models for predicting MPG (miles per gallon) based on vehicle features.
# The code utilizes the Lineapy library to store and retrieve model artifacts, ensuring reproducibility and tracking of data and models.
#
# @section components Key Components
#The project includes the following key components:
# - Saving and retrieving model artifacts using Lineapy.
# - Data cleaning and preparation.
# - Training of linear regression and DNN models.
# - Visualization of training loss.
#
# @section functions Functions
# - \ref plot_loss: Function to plot loss curves during training.
# - \ref build_and_compile_model: Function to build and compile a DNN model.
# - \ref save_model_as_artifact: Function to save a model as a Lineapy artifact.
#
# @section installation Installation Instructions
# 1. Install required dependencies: `pip install -r requirements.txt`
# 2. Run the main script to train and save models.
 


%%capture
import IPython
if (IPython.version_info[0] < 7):
    !pip -q install ipython --upgrade
    exit()  # Exit to restart the runtime and load the updated IPython version.
    # This is to allow for Colab runtime to restart before executing the next cell.

# Install required libraries
!pip install -q seaborn
!pip -q install lineapy

# Load necessary libraries
import os
import pickle
import lineapy
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt


class DataPreprocessing:
    """
    Class to handle data preprocessing, including loading and cleaning the dataset.
    """
    def __init__(self, url, column_names):
        """
        Initializes the DataPreprocessing class with dataset URL and column names.

        @param url: str The URL where the dataset is located.
        @param column_names: list The column names for the dataset.
        """
        self.url = url
        self.column_names = column_names
        self.dataset = self.load_data()

    def load_data(self):
        """
        Loads the dataset from the provided URL and preprocesses it.

        @return: pd.DataFrame The cleaned dataset.
        """
        raw_dataset = pd.read_csv(self.url, names=self.column_names, na_values='?', comment='\t',
                                  sep=' ', skipinitialspace=True)
        dataset = raw_dataset.copy()
        dataset = dataset.dropna()
        dataset['Origin'] = dataset['Origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
        dataset = pd.get_dummies(dataset, columns=['Origin'], prefix='', prefix_sep='')
        return dataset

    def split_data(self, dataset, train_frac=0.8):
        """
        Splits the dataset into training and test sets.

        @param dataset: pd.DataFrame The dataset to split.
        @param train_frac: float Fraction of the dataset to use for training.

        @return: Tuple[pd.DataFrame, pd.DataFrame] The training and test datasets.
        """
        train_dataset = dataset.sample(frac=train_frac, random_state=0)
        test_dataset = dataset.drop(train_dataset.index)
        return train_dataset, test_dataset


class ModelNormalization:
    """
    Class for normalizing the data to improve training performance.
    """
    def __init__(self, train_features):
        """
        Initializes the normalizer.

        @param train_features: np.ndarray The features used to fit the normalizer.
        """
        self.normalizer = tf.keras.layers.Normalization(axis=-1)
        self.normalizer.adapt(np.array(train_features))

    def normalize(self, features):
        """
        Normalizes the provided features.

        @param features: np.ndarray The features to normalize.

        @return: np.ndarray The normalized features.
        """
        return self.normalizer(features)


class ModelBuilder:
    """
    Class to build and compile TensorFlow models.
    """
    def __init__(self, norm_layer):
        """
        Initializes the ModelBuilder with a normalization layer.

        @param norm_layer: tf.keras.layers.Layer The normalization layer to use in the model.
        """
        self.norm_layer = norm_layer

    def build_linear_model(self):
        """
        Builds a simple linear regression model.

        @return: tf.keras.Sequential The compiled linear regression model.
        """
        model = tf.keras.Sequential([
            self.norm_layer,
            layers.Dense(units=1)
        ])
        model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.1), loss='mean_absolute_error')
        return model

    def build_dnn_model(self):
        """
        Builds a deep neural network (DNN) model.

        @return: tf.keras.Sequential The compiled DNN model.
        """
        model = keras.Sequential([
            self.norm_layer,
            layers.Dense(64, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(1)
        ])
        model.compile(loss='mean_absolute_error', optimizer=tf.keras.optimizers.Adam(0.001))
        return model


class TrainingPipeline:
    """
    Class to handle the training pipeline and save artifacts using lineapy.
    """
    def __init__(self, train_features, train_labels, test_features, test_labels, normalizer):
        """
        Initializes the training pipeline.

        @param train_features: np.ndarray The features used for training.
        @param train_labels: np.ndarray The labels corresponding to the training features.
        @param test_features: np.ndarray The features used for testing.
        @param test_labels: np.ndarray The labels corresponding to the test features.
        @param normalizer: tf.keras.layers.Normalization The normalization layer.
        """
        self.train_features = train_features
        self.train_labels = train_labels
        self.test_features = test_features
        self.test_labels = test_labels
        self.normalizer = normalizer
        self.model_artifact = None

    def save_artifacts(self):
        """
        Saves training, test data, and labels as artifacts using lineapy.
        """
        train_artifact = lineapy.save(self.train_features, "train_data")
        lineapy.save(self.train_labels, "train_labels")
        lineapy.save(self.test_features, "test_data")
        lineapy.save(self.test_labels, "test_labels")
        self.model_artifact = lineapy.save(self.normalizer, "normalizer")

    def get_model_code(self):
        """
        Retrieves the code for the model artifact.

        @return: str The code representation of the model artifact.
        """
        return prettify(self.model_artifact.get_code(use_lineapy_serialization=False))

    def run_pipeline(self, model_type='linear'):
        """
        Runs the pipeline with the specified model type.

        @param model_type: str The type of model to train ('linear' or 'dnn').

        @return: dict The results from the model evaluation.
        """
        model_builder = ModelBuilder(self.normalizer)
        if model_type == 'linear':
            model = model_builder.build_linear_model()
        elif model_type == 'dnn':
            model = model_builder.build_dnn_model()
        
        model.fit(self.train_features, self.train_labels, epochs=100, validation_split=0.2, verbose=0)
        test_results = model.evaluate(self.test_features, self.test_labels, verbose=0)
        
        return test_results


def plot_loss(history):
    """
    Plots the loss during training.

    @param history: tf.keras.callbacks.History The history object containing loss information.
    """
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 10])
    plt.xlabel('Epoch')
    plt.ylabel('Error [MPG]')
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin']
data_processor = DataPreprocessing(url, column_names)
dataset = data_processor.dataset
train_dataset, test_dataset = data_processor.split_data(dataset)

train_features = train_dataset[['Cylinders', 'Displacement', 'Horsepower', 'Weight']].values
train_labels = train_dataset['MPG'].values
test_features = test_dataset[['Cylinders', 'Displacement', 'Horsepower', 'Weight']].values
test_labels = test_dataset['MPG'].values

normalizer = ModelNormalization(train_features)

# Run the training pipeline
pipeline = TrainingPipeline(train_features, train_labels, test_features, test_labels, normalizer)
pipeline.save_artifacts()
test_results = pipeline.run_pipeline('dnn')

# Plot the loss curve for the DNN model
plot_loss(test_results)
