<<<<<<< HEAD
import pandas as pd
import warnings
import matplotlib.pyplot as plt


def EDA(data):
    """Perform exploratory data analysis on a given dataset.

    Args:
      data (pandas.DataFrame): The dataset to analyze.
    """
    # Check for missing values
    if data.isnull().values.any():
        # Find the number of missing values for each column
        missing_counts = data.isnull().sum()
        # Select only the columns with missing values
        missing_columns = missing_counts[missing_counts > 0]
        print(f"Missing values found in columns: {missing_columns}")
    else:
        print("No missing values found")

    # Check for outliers
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    if outliers.empty:
        print("No outliers found")
    else:
        print(f"Outliers found at positions: {outliers.index}")

    # Check data types
    data_types = data.dtypes
    print(f"Data types: {data_types}")

    # Check value counts for relevant columns
    relevant_values = ['yes', 'Yes', 'y', 'Y', 'no', 'No', 'n', 'N', 'Boy', 'Girl','boy','girl','g','b','G','B', 'Male', 'male', 'm', 'M', 'Female', 'female', 'f',
                       'F']
    for column in data.columns:
        if any(value in data[column].unique() for value in relevant_values):
            counts = data[column].value_counts()

    # Check correlations
    correlations = data.corr()
    print("Correlation table:")
    print(correlations)

    # Check for skewness
    skewness = data.skew()
    print("Skewness:")
    skewness.plot(kind='bar')
    plt.show()
=======
import pandas as pd
import warnings
import matplotlib.pyplot as plt


def EDA(data):
    """Perform exploratory data analysis on a given dataset.

    Args:
      data (pandas.DataFrame): The dataset to analyze.
    """
    # Check for missing values
    if data.isnull().values.any():
        # Find the number of missing values for each column
        missing_counts = data.isnull().sum()
        # Select only the columns with missing values
        missing_columns = missing_counts[missing_counts > 0]
        print(f"Missing values found in columns: {missing_columns}")
    else:
        print("No missing values found")

    # Check for outliers
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    if outliers.empty:
        print("No outliers found")
    else:
        print(f"Outliers found at positions: {outliers.index}")

    # Check data types
    data_types = data.dtypes
    print(f"Data types: {data_types}")

    # Check value counts for relevant columns
    relevant_values = ['yes', 'Yes', 'y', 'Y', 'no', 'No', 'n', 'N', 'Boy', 'Girl','boy','girl','g','b','G','B', 'Male', 'male', 'm', 'M', 'Female', 'female', 'f',
                       'F']
    for column in data.columns:
        if any(value in data[column].unique() for value in relevant_values):
            counts = data[column].value_counts()

    # Check correlations
    correlations = data.corr()
    print("Correlation table:")
    print(correlations)

    # Check for skewness
    skewness = data.skew()
    print("Skewness:")
    skewness.plot(kind='bar')
    plt.show()
>>>>>>> 9a926d635a4e8c56ba8dc40f6ee178c59df63b95
