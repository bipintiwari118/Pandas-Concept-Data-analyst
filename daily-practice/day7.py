#Python Pandas Cleaning Data 
# Data cleaning is an essential step in the data analysis process. It involves identifying and handling missing values, outliers, and duplicate data to ensure the quality and accuracy of the analysis. Pandas provides several functions to clean and preprocess data in a DataFrame. Some of the commonly used functions are:
#bad data could  be missing values,wrong data, outliers, or duplicate data. Cleaning the data helps to improve the quality of the analysis and ensures that the results are accurate and reliable.
#Pandas provides several functions to clean and preprocess data in a DataFrame. Some of the commonly used functions are:
# 1. dropna() - Removes missing values from the DataFrame
# 2. fillna() - Fills missing values with a specified value or method
# 3. drop_duplicates() - Removes duplicate rows from the DataFrame
import pandas as pd

#empty cells are considered as missing values in Pandas. The dropna() function is used to remove missing values from the DataFrame. By default, it removes any row that contains at least one missing value. You can also specify the axis parameter to remove columns with missing values instead of rows.
df=pd.read_csv('daily-practice\dirtydata.csv')
print(df.info())
emp=df.dropna()
print(emp.to_string())



# The fillna() function is used to fill missing values in the DataFrame with a specified value or method. You can use this function to replace missing values with a constant value, the mean, median, or mode of the column, or use forward or backward filling methods.
# Filling missing values with a constant value 

df=pd.read_csv('daily-practice\dirtydata.csv')
fill=df.fillna(0)
print(fill.to_string())

#to replace the empty value for one column 
df=pd.read_csv('daily-practice\dirtydata.csv')
df=df['Calories'].fillna(0)
print(df.to_string())




# here we replace the empty value with the mean of the column mean(), median(), and mode() functions are used to calculate the mean, median, and mode of a column in a DataFrame, respectively. These functions can be used to fill missing values in a column with the mean, median, or mode of that column.

#calculate the mean and fill the empty value with it

df=pd.read_csv('daily-practice\dirtydata.csv')
a=df['Calories'].mean()
df['Calories']=df['Calories'].fillna(a)
print(df.to_string())


#inplace parameter is used to modify the original DataFrame without creating a new one. When inplace=True is set, the changes are made directly to the original DataFrame, and the function returns None. If inplace=False (the default), a new DataFrame is returned with the changes, and the original DataFrame remains unchanged.
# Filling missing values with the mean of the column using inplace=True
# df=pd.read_csv('daily-practice\dirtydata.csv')
# a=df['Calories'].mean()
# df['Calories'].fillna(a,inplace=True)
# print(df.to_string())


#median
df=pd.read_csv('daily-practice\dirtydata.csv')
a=df['Calories'].median()
df['Calories']=df['Calories'].fillna(a)
print(df.to_string())
