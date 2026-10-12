import pandas as pd

df = pd.read_excel("E:\\Django_Python\\python_start\\CountryData_records.xlsx")

print(df.describe())# Descriptive statistics for numerical columns it wont include non-numerical columns like CountryName, CountryCode, and IncomeGroup(categoriacl data like strings like object dtype)
#         BirthRate  InternetUsers
# count  200.000000     200.000000
# mean    19.942875      60.172253
# std     10.091588      28.792191
# min      5.500000       1.300000
# 25%     10.975000      36.825000
# 50%     17.784500      65.500000
# 75%     27.000000      86.700000
# max     45.985000     100.000000

print(df.describe().transpose())# Descriptive statistics for numerical columns it wont include non-numerical columns like CountryName, CountryCode, and IncomeGroup(categoriacl data like strings like object dtype)

print(df.describe(include="all").transpose())# Descriptive statistics for all columns including non-numerical ones like CountryName, CountryCode, and IncomeGroup(categoriacl data like strings like object dtype)

dfn = df[["BirthRate", "InternetUsers"]]
print(dfn.describe().transpose())# Descriptive statistics for numerical columns it wont include non-numerical columns like CountryName, CountryCode, and IncomeGroup(categoriacl data like strings like object dtype)
# will give same as above bcz this also includes only numerical columns.-
dfo = df[["CountryName", "CountryCode", "IncomeGroup"]]
print(dfo.describe().transpose())# Descriptive statistics for non-numerical columns it will include only non-numerical columns like CountryName, CountryCode, and IncomeGroup(categoriacl data like strings like object dtype)
#             count unique          top freq
# CountryName   200    200        Aruba    1
# CountryCode   200    200          ABW    1
# IncomeGroup   200      4  High income   64

# above is put put of non numerical columns result