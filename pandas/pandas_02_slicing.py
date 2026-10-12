import pandas as pd

print(pd.__version__)

df = pd.read_excel("E:\\Django_Python\\python_start\\CountryData_records.xlsx")

print(df.head()) #Prints the first 5 rows of the DataFrame by default
print(df.tail()) #Prints the last 5 rows of the DataFrame by default

print(df[0:2])
#    CountryName CountryCode  BirthRate  InternetUsers  IncomeGroup
# 0        Aruba         ABW     10.244           78.9  High income
# 1  Afghanistan         AFG     35.253            5.9   Low income

print(df[::-1])

#  CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup
# 199                Guinea         GIN     20.650          66.04  Upper middle income
# 198                 Gabon         GAB     31.026          35.93           Low income
# 197               Liberia         LBR     13.465          43.66  Lower middle income
# 196               Lesotho         LSO     24.148          72.07  Upper middle income
# 195      Papua New Guinea         PNG     16.493          12.01           Low income
# ..                    ...         ...        ...            ...                  ...
# 4    United Arab Emirates         ARE     11.044          88.00          High income
# 3                 Albania         ALB     12.877          57.20  Upper middle income
# 2                  Angola         AGO     45.985          19.10  Upper middle income
# 1             Afghanistan         AFG     35.253           5.90           Low income
# 0                   Aruba         ABW     10.244          78.90          High income

# [200 rows x 5 columns]

print(df[0:199:24])
#            CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup
# 0                Aruba         ABW     10.244          78.90          High income
# 24              Brazil         BRA     13.700          81.30  Upper middle income
# 48                Fiji         FJI     21.000          75.00  Upper middle income
# 72     Kyrgyz Republic         KGZ     23.000          40.00  Lower middle income
# 96            Malaysia         MYS     16.000          97.00  Upper middle income
# 120          Singapore         SGP      8.000          96.00          High income
# 144         Uzbekistan         UZB     23.000          55.00  Lower middle income
# 168           Guernsey         GGY     43.741          90.35          High income
# 192  Wallis and Futuna         WLF     17.363          87.29          High income

# how to get only some columns:
# ==================================

print(df["CountryName"])
# 0                     Aruba
# 1               Afghanistan
# 2                    Angola
# 3                   Albania
# 4      United Arab Emirates
#                ...         
# 195        Papua New Guinea
# 196                 Lesotho
# 197                 Liberia
# 198                   Gabon
# 199                  Guinea
# Name: CountryName, Length: 200, dtype: str

#How to get multiple columns:
# =======================================
print(df[["CountryName", "BirthRate"]])
#     CountryName  BirthRate
# 0                   Aruba     10.244
# 1             Afghanistan     35.253
# 2                  Angola     45.985
# 3                 Albania     12.877
# 4    United Arab Emirates     11.044
# ..                    ...        ...
# 195      Papua New Guinea     16.493
# 196               Lesotho     24.148
# 197               Liberia     13.465
# 198                 Gabon     31.026
# 199                Guinea     20.650

# [200 rows x 2 columns]
print(df[23:24]) 
#    CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup
# 23     Bolivia         BOL       24.1           39.7  Lower middle income

print(df.dtypes) # Gives columns with data types
# CountryName          str
# CountryCode          str
# BirthRate        float64
# InternetUsers    float64
# IncomeGroup          str
# dtype: object

print(df.head(2))# prints first 2 rows of the DataFrame
#     CountryName CountryCode  BirthRate  InternetUsers  IncomeGroup
# 0        Aruba         ABW     10.244           78.9  High income
# 1  Afghanistan         AFG     35.253            5.9   Low income

print(df[["CountryName", "CountryCode", "IncomeGroup"]])
#               CountryName CountryCode          IncomeGroup
# 0                   Aruba         ABW          High income
# 1             Afghanistan         AFG           Low income
# 2                  Angola         AGO  Upper middle income
# 3                 Albania         ALB  Upper middle income
# 4    United Arab Emirates         ARE          High income
# ..                    ...         ...                  ...
# 195      Papua New Guinea         PNG           Low income
# 196               Lesotho         LSO  Upper middle income
# 197               Liberia         LBR  Lower middle income
# 198                 Gabon         GAB           Low income
# 199                Guinea         GIN  Upper middle income
print(df[[ "BirthRate", "InternetUsers"]])
#     BirthRate  InternetUsers
# 0     10.244           78.9
# 1     35.253            5.9
# 2     45.985           12.3
# 3     12.877           67.4
# 4     11.044           80.1
# ..       ...            ...
# 195   16.493           23.4
# 196   24.148           19.8
# 197   13.465           11.2
# 198   31.026           45.6
# 199   20.650           34.7

# [200 rows x 2 columns]




#How to change column alias names:
# =============================================

print(df.columns)

# Index(['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers',
#        'IncomeGroup'],
#       dtype='str')
df.columns = ["a", "b", "c", "d", "e"]
print(df.head(3))
#                       a    b       c     d                    e
# 0                 Aruba  ABW  10.244  78.9          High income
# 1           Afghanistan  AFG  35.253   5.9           Low income
# 2                Angola  AGO  45.985  19.1  Upper middle income

df.rename(columns={"a": "CN", "b": "CC", "c": "BR", "d": "IU", "e": "IG"}, inplace=True)
print(df.head(3))
# You can use the `rename` method to change column names
# ==========================================================
#             CN   CC      BR    IU                   IG
# 0        Aruba  ABW  10.244  78.9          High income
# 1  Afghanistan  AFG  35.253   5.9           Low income
# 2       Angola  AGO  45.985  19.1  Upper middle income

# How to create new columns with existing columns:
# =============================================

df["BR_plus_IU"] = df["BR"] + df["IU"]
print(df.head(3))
# ==========================================================
#             CN   CC      BR    IU                   IG  BR_plus_IU
# 0        Aruba  ABW  10.244  78.9          High income       89.144
# 1  Afghanistan  AFG  35.253   5.9           Low income       41.153
# 2       Angola  AGO  45.985  19.1  Upper middle income       65.085

df["BR_Into_IU"] = df["BR"] * df["IU"]
print(df.head(3))
# ==========================================================
#             CN   CC      BR    IU                   IG  BR_plus_IU  BR_Into_IU
# 0        Aruba  ABW  10.244  78.9          High income      89.144    808.2516
# 1  Afghanistan  AFG  35.253   5.9           Low income      41.153    207.9927
# 2       Angola  AGO  45.985  19.1  Upper middle income      65.085    878.3135
# =============================================================================
df["BR_div_IU"] = df.BR / df.IU
print(df.head(3))
#             CN   CC      BR    IU                   IG  BR_plus_IU  BR_Into_IU  BR_div_IU
# 0        Aruba  ABW  10.244  78.9          High income      89.144    808.2516   0.129835
# 1  Afghanistan  AFG  35.253   5.9           Low income      41.153    207.9927   5.975085
# 2       Angola  AGO  45.985  19.1  Upper middle income      65.085    878.3135   2.407592
# ===================================================================================================


# How to Remove columns:
# =============================

print(df)
#                       CN   CC      BR     IU                   IG  BR_plus_IU  BR_Into_IU  BR_div_IU
# 0                   Aruba  ABW  10.244  78.90          High income      89.144   808.25160   0.129835
# 1             Afghanistan  AFG  35.253   5.90           Low income      41.153   207.99270   5.975085
# 2                  Angola  AGO  45.985  19.10  Upper middle income      65.085   878.31350   2.407592
# 3                 Albania  ALB  12.877  57.20  Upper middle income      70.077   736.56440   0.225122
# 4    United Arab Emirates  ARE  11.044  88.00          High income      99.044   971.87200   0.125500
# ..                    ...  ...     ...    ...                  ...         ...         ...        ...
# 195      Papua New Guinea  PNG  16.493  12.01           Low income      28.503   198.08093   1.373272
# 196               Lesotho  LSO  24.148  72.07  Upper middle income      96.218  1740.34636   0.335063
# 197               Liberia  LBR  13.465  43.66  Lower middle income      57.125   587.88190   0.308406
# 198                 Gabon  GAB  31.026  35.93           Low income      66.956  1114.76418   0.863512
# 199                Guinea  GIN  20.650  66.04  Upper middle income      86.690  1363.72600   0.312689

# [200 rows x 8 columns]

#axis=0 means rows, axis=1 means columns
# =====================================================================================================
df.drop("BR_div_IU", axis=1, inplace=True) 
print(df.head(3))
#             CN   CC      BR    IU                   IG  BR_plus_IU  BR_Into_IU
# 0        Aruba  ABW  10.244  78.9          High income      89.144    808.2516
# 1  Afghanistan  AFG  35.253   5.9           Low income      41.153    207.9927
# 2       Angola  AGO  45.985  19.1  Upper middle income      65.085    878.3135