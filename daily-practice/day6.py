#Python Pandas Viewing & Analyzing DataFrames 
#Pandas provides several functions to view and analyze DataFrames. Some of the commonly used functions are: 
# 1. head() - Returns the first n rows of the DataFrame
# 2. tail() - Returns the last n rows of the DataFrame
# 3. info() - Provides information about the DataFrame
# 4. describe() - Provides statistical summary of the DataFrame
import pandas as pd


#1. head() - Returns the first n rows of the DataFrame

df=pd.read_csv('daily-practice\data.csv')
print(df.head()) #by default it returns the first 5 rows
print(df.head(10)) #it returns the first 3 rows



#2. tail() - Returns the last n rows of the DataFrame

print(df.tail()) #by default it returns the last 5 rows
print(df.tail(10)) #it returns the last 10 rows



#3. info() - Provides information about the DataFrame 
# The info() function provides information about the DataFrame, including the number of non-null values, data types of each column, and memory usage. This function is useful for understanding the structure of the DataFrame and identifying any missing values or data type issues.

print(df.info())