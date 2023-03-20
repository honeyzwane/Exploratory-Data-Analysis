import pandas as pd
import warnings
import matplotlib.pyplot as plt

#A simple code to analyse the dataset

import pandas as pd
import warnings

warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt


def EDA(data):
    """Perform exploratory data analysis on a given dataset.
    Args:
      data (pandas.DataFrame): The dataset to analyze.
    """
    from IPython.display import display
    display(data.head())

    # Print the shape of the dataset
    print(f"Number of rows: {data.shape[0]}")
    print(f"Number of columns: {data.shape[1]}")

    # Check for missing values
    if data.isnull().values.any():
        # Find the number of missing values for each column
        missing_counts = data.isnull().sum()
        # Calculate the percentage of missing values for each column
        missing_percentages = 100 * missing_counts / len(data)
        # Select only the columns with missing values
        missing_columns = missing_percentages[missing_percentages > 0]
        print(f"Percentage of missing values in each column:")
        print(missing_columns)
    else:
        print("No missing values found")

    # Check for duplicated rows
    duplicates = data[data.duplicated()]
    if duplicates.empty:
        print("No duplicated rows found")
    else:
        duplicate_count = len(duplicates)
        total_count = len(data)
        print(
            f"{duplicate_count} out of {total_count} rows are duplicated ({100 * duplicate_count / total_count:.2f}%)")

    # Check for outliers
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    outliers = ((data < lower_bound) | (data > upper_bound)).sum()
    if outliers.sum() == 0:
        print("No outliers found")
    else:
        print(f"Number of outliers per column:")
        print(outliers)

    # Check data types
    data_types = data.dtypes
    print(f"Data types: {data_types}")

    # Check correlations
    correlations = data.corr()
    print("Correlation table:")
    print(correlations)
