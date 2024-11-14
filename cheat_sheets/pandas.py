import pandas as pd

# How to build a dictionary :
# # Keys = Column labels
# # Values = Corresponding data in list form, column by column
dict = { 'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
           'capital': ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
           'area': [8.516, 17.10, 3.286, 9.597, 1.221],
           'population': [200.4, 143.5, 1252, 1357, 52.98] }
# # Or from lists + a dict :
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country' : names, 
 'drives_right' : dr,
 'cars_per_cap' : cpc }

brics = pd.DataFrame(dict)

# Automatically, the row labels are set to 0, 1, 2 ... 
# To specify them, set the index attribute to a list of labels : 
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# OR import data from an external .csv file containing the data
# CSV = coma separated values
brics = pd.read_csv("path/to/brics.csv")

# Precision can be given that the 1st column contains row indexes :
brics = pd.read_csv("path/to/brics.csv", index_col = 0)

print(brics)

    #          country  drives_right  cars_per_cap
    # US  United States          True           809
    # AU      Australia         False           731
    # JA          Japan         False           588
    # IN          India         False            18
    # RU         Russia          True           200
    # MO        Morocco          True            70
    # EG          Egypt          True            45

# Column access : 
brics["country"]
# Returns a pandas.core.series.Series, 1D labelled array

# Several column access :
brics["country", "capital"]
# Returns a DataFrame with 2 columns

# Row access :
brics[1:4]
array[rows, columns]
# 2nd one is still exclusive

# loc : label-based
# iloc : integer position-based
brics.loc["RU"]
brics.iloc[4]
# Returns a pandas serie containung info about 1 row, but in a column
brics.loc[["RU"]]
brics.iloc[[4]]
# Returns a pandas serie containing the info in a single row
brics.loc[["RU", "IN", "US"]]
brics.iloc[[4, 3, 1]]
# Possibility to select multiple rows
brics.loc[["RU", "IN", "US"], ["country", "capital"]]
brics.iloc[[4, 3, 1], [0, 1]]
# Possibility to keep only certain columns, the intersection is returned
brics.loc[:, ["country", "capital"]]
# Possibility to select all rows but only certain columns
