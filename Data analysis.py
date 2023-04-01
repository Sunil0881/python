# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('your_dataset.csv')

# Show the first few rows of the dataset
print(data.head())

# Check the shape of the dataset
print('Dataset shape:', data.shape)

# Check the data types of columns
print('Data types:', data.dtypes)

# Check for missing values
print('Missing values:', data.isnull().sum())

# Check for duplicated rows
print('Duplicated rows:', data.duplicated().sum())

# Get summary statistics of numerical columns
print('Summary statistics:', data.describe())

# Plot a histogram of a column
plt.hist(data['column_name'])
plt.xlabel('Column Name')
plt.ylabel('Frequency')
plt.title('Histogram Column Name')
plt.show()

# Plot a scatter plot between two columns
sns.scatterplot(x='column1', y='column2', data=data)
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.title('Scatter plot between Column 1 and Column 2')
plt.show()

# Plot a boxplot of a column
sns.boxplot(x='column_name', data=data)
plt.xlabel('Column Name')
plt.title('Boxplot Column Name')
plt.show()

# Compute correlation matrix between columns
corr_matrix = data.corr()
print('Correlation matrix:', corr_matrix)
