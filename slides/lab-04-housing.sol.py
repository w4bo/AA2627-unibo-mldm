import numpy as np
import pandas as pd

housing = pd.read_csv("https://raw.githubusercontent.com/w4bo/handsOnDataPipelines/main/materials/datasets/housing.csv", delimiter=",")

# Add new columns
housing['population_per_household'] = housing['population'] / housing['households']
housing['rooms_per_household'] = housing['total_rooms'] / housing['households']
housing['bedrooms_per_room'] = housing['total_bedrooms'] / housing['total_rooms']

# Fill missing values with the median
for column in housing.columns:
    if housing[column].isnull().any():  # Check if there are missing values
        median_value = housing[column].median()  # Calculate median
        housing[column].fillna(median_value, inplace=True)  # Fill missing values with median

# Standardize all numeric columns
numeric_columns = housing.select_dtypes(include=[np.number]).columns  # Select numeric columns
for column in numeric_columns:
    mean_value = housing[column].mean()  # Calculate mean
    std_value = housing[column].std()  # Calculate standard deviation
    housing[column] = (housing[column] - mean_value) / std_value  # Standardize

# One-hot encode 'ocean_proximity'
housing = pd.get_dummies(housing, columns=['ocean_proximity'], drop_first=True)

# Now 'housing' is your processed DataFrame
housing