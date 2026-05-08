#Python Pandas Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). It is similar to a column in a spreadsheet or a SQL table. Each element in a Series has an associated label, which can be used to access the data.

import pandas as pd

a=[1, 2, 3, 4, 5]
s = pd.Series(a)
print(s)


#use dictionary to create series
data = {'a': 10, 'b': 20, 'c': 30}
s = pd.Series(data)
print(s)


#dataframe is a 2-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or a SQL table. A DataFrame is a collection of Series, where each Series represents a column in the DataFrame. 
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print(df)