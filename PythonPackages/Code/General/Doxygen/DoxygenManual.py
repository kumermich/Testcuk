"""! @brief Python program showcasing Doxygen-style comments for documentation purposes."""

############################
# Author: Sadegh Naderi
# Date created: 30.07.2023
# Path: BA23-14-Packages\report\Code\General\Doxygen\DoxygenManual.py
# Version: 3.0
# Reviewed by: Sadegh Naderi
# Review Date: 16.08.2023
############################

##
# @mainpage Python Packages project
#
# @section author Author
# - Created by Sadegh Naderi on 30.07.2023.
# - Modified by Sadegh Naderi on 04.08.2023.
#
# @section intro_sec Introduction
#
# This documentation serves as a guide to understand how to document the code with Doxygen comments, different 
# regression Algorithms, and the Flask and pdf2txt Python packages. 
#
# @section documentation A guide to documenting the code using Doxygen
# 
# The codebase aims to provide a comprehensive guide on how to utilize Doxygen to document Python programs 
# effectively.
#
# @section regression Regression algorithms
# 
# The code for Regression algorithms provided here aims to explore seven of the most widely used regression 
# algorithms in Python and Machine Learning. These include Linear Regression, Polynomial Regression, Ridge 
# Regression, Lasso Regression, Elastic Net Regression, Decision Tree-based methods, and Support Vector 
# Regression (SVR).
# 
# @subsection loading Data loading
#
# The diabetes dataset is one of the built-in datasets provided by the scikit-learn library (sklearn) 
# in Python. scikit-learn is a popular machine learning library that offers various tools for data analysis and 
# modeling.
#
# @subsection evaluation Model evaluation and visualization
#
# The codebase evaluates the performance of the trained model using evaluation metrics such as R2 score and
# mean squared error (MSE). It also provides visualizations, including scatter plots enabling users to 
# assess the accuracy of the prediction functions. 
# 
# @image html polynomialRegressionPlot.png "polynomial regression plot" width=500px
# 
# Coefficient curves are provided where relevant, to understand the effect of regularization in regression models.
#
# @image html ridgeCoefficientsvsAlphaPlot.png "Ridge regression coefficient curves" width=500px
# 
# @section packages Introduction to Flask and pdf2txt Python packages.
# 
# In this codebase the Flask package is used to write a simple web application.
# 
# @image html FlaskHomePage.png "The view of the home page" width=500px
#
# the pdf2txt package is used to extract data from pdf files, in our case, a CV pdf file.
# 
# @section timeseries 
# 
# A basic example of time series forecasting using a machine learning approach with Python is provided and the
# output of the forecast is plotted.
# 
# @image html timeSeriesForecast.png "Time series forecasting with linear regression" width=500px
#
# @section start Getting Started
#
# @warning To get started with the codebase, ensure that you have the required packages installed.
# @note The information about the packages is provided in the documentation of each file.
# Once the dependencies are set up, you can follow the step-by-step instructions in the codebase.


##
# @file DoxygenManual.py
#
# @brief This is a sample module for demonstrating Doxygen documentation in Python.
#
#  This code file is created in order to provide a summarized manual on how to use doxygen to document Python files.
#
# @section description_of_file Description
#
# This file contains a simple class "Person" representing a person with their name and age. It also includes a
# function "add_numbers" to add two numbers.
#
# @note This is a sample Python file demonstrating how to use Doxygen to document Python code.
# @warning This code is for demonstration purposes only and may not be functionally complete or optimized.
# Running this file does not lead to a specific result or address a specific need.
#
# @section authors Author
# - Created by Sadegh Naderi on 30.07.2023.
# - Modified by Sadegh Naderi on 04.08.2023.
#

## @brief This is a simple class representing a person.
#  The class holds information about a person's name and age.
class Person:
    """!This is a simple class representing a person.
    The class holds information about a person's name and age.
    """

    def __init__(self, name, age):
        """!The constructor.
        @param name The name of the person.
        @param age The age of the person.
        """
        ## @var name
        #  @brief The name of the person.
        self.name = name
        ## @var age
        #  @brief The age of the person.
        self.age = age

    def get_name(self):
        """!A method to get the person's name.
        @return The name of the person.
        """
        return self.name

    def set_age(self, age):
        """!A method to set the person's age.
        @param age The age of the person.
        """
        self.age = age

    def get_age(self):
        """!A method to get the person's age.
        @return The age of the person.
        """
        return self.age


def add_numbers(x, y):
    """! This function adds two numbers.
    The function takes two numbers as parameters and returns their sum.

    @note This function assumes that the inputs `x` and `y` are numeric data types.
    It may not produce correct results if non-numeric data is provided as input.

    @warning Be cautious when using this function with large numbers or floating-point numbers,
    as it may lead to potential precision issues in the addition operation.

    @param x The first number.
    @param y The second number.
    @return The sum of the two numbers.
    """
    return x + y

if __name__ == "__main__":

    ## @var person
    #  @brief A Person object representing an individual.
    #
    #  This variable holds an instance of the Person class with the name "Alice" and age 30.
    person = Person("Alice", 30)

    ## @var name
    #  @brief The name of the person.
    name = person.get_name()
    print("Name:", name)

    ## @var age
    #  @brief The age of the person.
    age = person.get_age()
    print("Age:", age)

    ## @var num1
    #  @brief The first number for addition.
    #
    #  This variable holds the value 5, which will be used as the first operand for the add_numbers function.

    ## @var num2
    #  @brief The second number for addition.
    #
    #  This variable holds the value 10, which will be used as the second operand for the add_numbers function.

    num1 = 5
    num2 = 10
    ## @var result
    #  @brief The sum of the two numbers.
    #  This variable holds the result of calling the \ref add_numbers "add_numbers()" function with `num1` and `num2` as inputs.
    result = add_numbers(num1, num2)
    print("Sum:", result)
