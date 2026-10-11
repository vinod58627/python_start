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