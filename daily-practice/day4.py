#Pandas Read CSV
#Pandas provides a powerful function called read_csv() to read data from a CSV file and create a DataFrame. The read_csv() function takes the file path as an argument and returns a DataFrame containing the data from the CSV file.
import pandas as pd
# loadig the CSV file into a DataFrame
df=pd.read_csv('daily-practice\data.csv')
print(df.to_string())
print(df)


#max_rows and max_columns
#Pandas has two options, max_rows and max_columns, that allow you to control the number of rows and columns displayed when printing a DataFrame. By default, Pandas will display a maximum of 60 rows and 20 columns. If your DataFrame has more than these limits, it will truncate the output and show only the first few and last few rows or columns.
#You can change these limits using the pd.set_option() function. For example, to display all rows and columns, you can set max_rows and max_columns to None:

print(pd.options.display.max_rows)
print(pd.options.display.max_columns)

#we can change the default value of max_rows and max_columns to None to display all rows and columns in the DataFrame
pd.options.display.max_rows = 99999
print(df)


