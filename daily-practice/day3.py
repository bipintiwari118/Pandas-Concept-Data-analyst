#Python Pandas DataFrames are two-dimensional labeled data structures with columns of potentially different types. They are similar to spreadsheets or SQL tables. A DataFrame is a collection of Series, where each Series represents a column in the DataFrame.
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print(df)

#location-based indexing
print(df.loc[0]) #access the first row of the DataFrame 
print(df.loc[1:3]) #access rows from index 1 to 3 (inclusive)
#label-based indexing
print(df.iloc[0]) #access the first row of the DataFrame
print(df.iloc[1:3]) #access rows from index 1 to 3 (exclusive)
