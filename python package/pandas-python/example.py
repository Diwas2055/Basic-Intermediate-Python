
#! DataFrame in Pandas Python

# A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion 
# in rows and columns.

#?  Features of DataFrame :- 

    # Potentially columns are of different types
    # Size – Mutable
    # Labeled axes (rows and columns)
    # Can Perform Arithmetic operations on rows and columns

#?  Syntax :- 

# pandas.DataFrame( data, index, columns, dtype, copy)

# data :-   data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.
# index :-  For the row labels, the Index to be used for the resulting frame is Optional Default np.arange(n) if no index is passed.
# columns :- For column labels, the optional default syntax is - np.arange(n). This is only true if no index is passed.
# dtype :-  Data type of each column.
# copy :-  This command (or whatever it is) is used for copying of data, if the default is False.

#? Create DataFrame :-

# A pandas DataFrame can be created using various inputs like −
    # Lists
    # dict
    # Series
    # Numpy ndarrays
    # Another DataFrame


#? Create a DataFrame from Lists

# Example 1 :-

import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df)

# Example 2 :-

import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)

#? Create a DataFrame from Dict of ndarrays / Lists

import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print (df)

#? Create a DataFrame from List of Dicts

import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print (df1)
print (df2)

#? Create a DataFrame from Dict of Series

import pandas as pd
 
# Initialize data to Dicts of series.
d = {'one': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd']),
     'two': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd'])}
 
# creates Dataframe.
df = pd.DataFrame(d)
 
# print the data.
print (df)