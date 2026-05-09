#Python Pandas Cleaning Data of Wrong Format 
# In addition to handling missing values, data cleaning also involves identifying and correcting wrong data formats. This can include incorrect data types, inconsistent formatting, or invalid values. Pandas provides several functions to clean and preprocess data in a DataFrame. Some of the commonly used functions are:
# 1. astype() - Converts the data type of a column to a specified type
# 2. to_datetime() - Converts a column to datetime format
# 3. to_numeric() - Converts a column to numeric format
import pandas as pd

df=pd.read_csv('daily-practice\dirtydata.csv')
print(df.to_string())


# The astype() function is used to convert the data type of a column to a specified type. This can be useful when you have columns with incorrect data types that need to be converted to the appropriate type for analysis. For example, if you have a column that contains numeric values but is stored as a string, you can use astype() to convert it to a numeric data type.



#now lets try to date column to datetime format
df=pd.read_csv('daily-practice\dirtydata.csv')
df['Date']=pd.to_datetime(df['Date'])
print(df.to_string(),format('mixed'))
