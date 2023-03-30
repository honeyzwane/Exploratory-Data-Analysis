# Exploratory-Data-Analysis
For this task, I have created a script for EDA. this script can be imported anywhere and used to go through a basic exploration of data. the python script does the following: 

Returns the first five rows of the dataset using the display function from IPython.
Returns the number of rows and columns in the dataset using the shape attribute of the pandas DataFrame.
Checks if there are any missing values in the dataset using the isnull().values.any() method. If there are missing values, it - finds the number and percentage of missing values in each column and prints them.
Checks for duplicated rows using the duplicated() method. If there are duplicated rows, it prints the number of duplicated rows and their percentage.
Checks for outliers in the dataset using the interquartile range (IQR) method. It calculates the lower and upper bounds and - - checks for values that are less than the lower bound or greater than the upper bound. If there are outliers, it prints the number of outliers per column.
Checks the data types of each column using the dtypes attribute of the pandas DataFrame.
Calculates the correlation matrix for the dataset using the corr() method and prints it

I hope this makes someone's job a little simpler out there.
