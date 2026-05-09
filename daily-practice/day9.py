#Python Pandas Cleaning & Fixing Wrong Data
# In addition to handling missing values, data cleaning also involves identifying and correcting wrong data formats. This can include incorrect data types, inconsistent formatting, or invalid values. Pandas provides several functions to clean and preprocess data in a DataFrame. Some of the commonly used functions are:


import pandas as pd

df=pd.read_csv('daily-practice\dirtydata.csv')
print(df.to_string())


df.loc[7,'Duration']=45
print(df.to_string())


#for large dataset we can use the loc function to replace the wrong value with the correct one. The loc function is used to access a group of rows and columns by labels or a boolean array. In this case, we are using it to access the row with index 7 and the column 'Duration' to replace the wrong value with the correct one (45 in this case).
#now we will loop through the 'Duration' column and replace any value that is greater than 60 with 60, as it is unlikely that a workout session would last longer than 60 minutes.

df=pd.read_csv('daily-practice\dirtydata.csv')
print(df.to_string())

for i in df.index:
    if df.loc[i,'Duration']>120:
        df.loc[i,'Duration']=120

print(df.to_string())


#remove the row with index 7 using the drop() function. The drop() function is used to remove rows or columns from a DataFrame. In this case, we are using it to remove the row with index 7, which contains the wrong value for 'Duration'.

df=pd.read_csv('daily-practice\dirtydata.csv')
print(df.to_string())

for i in df.index:
    if df.loc[i,'Duration']>120:
        df.drop(i,inplace=True)

print(df.to_string())
        