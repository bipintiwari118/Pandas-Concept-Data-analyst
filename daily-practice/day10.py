#Python Pandas Removing Duplicates
# Duplicate data can occur in a dataset due to various reasons, such as data entry errors, merging datasets, or collecting data from multiple sources. Removing duplicates is an important step in the data cleaning process to ensure the accuracy and reliability of the analysis. Pandas provides several functions to remove duplicates from a DataFrame. Some of the commonly used functions are:
# 1. drop_duplicates() - Removes duplicate rows from the DataFrame
import pandas as pd
df=pd.read_csv('daily-practice\dirtydata.csv')
print(df.to_string())

# Remove duplicates
df.drop_duplicates(inplace=True)
print(df.to_string())