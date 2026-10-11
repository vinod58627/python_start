import pandas as pd

print(pd.__version__)

df = pd.read_excel("E:\\Django_Python\\python_start\\CountryData_records.xlsx")

print(df)
print(df.shape) #(200, 5) means 200 rows and 5 columns
print(df.columns) #Index(['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers',
    #    'IncomeGroup'],
    #   dtype='str')

print(len(df)) #200 means there are 200 rows in the DataFrame

print(df.head()) #Prints the first 5 rows of the DataFrame by default
print(df.tail()) #Prints the last 5 rows of the DataFrame by default

print(df.isnull()) #Prints a DataFrame of the same shape as df with True for NaN values and False otherwise
#Both are same
print(df.isna()) #Prints a DataFrame of the same shape as df with True for NaN values and False otherwise
print(df.isnull().sum()) #Prints the number of NaN values in each column

#    CountryName  CountryCode  BirthRate  InternetUsers  IncomeGroup
# 0          False        False      False          False        False
# 1          False        False      False          False        False
# 2          False        False      False          False        False
# 3          False        False      False          False        False
# 4          False        False      False          False        False
# ..           ...          ...        ...            ...          ...
# 195        False        False      False          False        False
# 196        False        False      False          False        False
# 197        False        False      False          False        False
# 198        False        False      False          False        False
# 199        False        False      False          False        False

# [200 rows x 5 columns]
# CountryName      0
# CountryCode      0
# BirthRate        0
# InternetUsers    0
# IncomeGroup      0
# dtype: int64

print(df.isna().sum()) #Prints the number of NaN values in each column
print(df.info()) #Prints a concise summary of the DataFrame, including the number of non-null entries and data types

# RangeIndex: 200 entries, 0 to 199
# Data columns (total 5 columns):
#  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   CountryName    200 non-null    str    
#  1   CountryCode    200 non-null    str    
#  2   BirthRate      200 non-null    float64
#  3   InternetUsers  200 non-null    float64
#  4   IncomeGroup    200 non-null    str    
# dtypes: float64(2), str(3)
# memory usage: 7.9 KB
# None