import pandas as pd

df = pd.read_excel("E:\\Django_Python\\python_start\\CountryData_records.xlsx")

print(df)

print(df["InternetUsers"]>50)
#0       True
# 1      False
# 2      False
# 3       True
# 4       True
#        ...  
# 195    False
# 196     True
# 197    False
# 198    False
# 199     True
# Name: InternetUsers, Length: 200, dtype: bool

print(df[df["InternetUsers"]>50])
#                       CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup
# 0                           Aruba         ABW     10.244          78.90          High income
# 3                         Albania         ALB     12.877          57.20  Upper middle income
# 4            United Arab Emirates         ARE     11.044          88.00          High income
# 5                       Argentina         ARG     17.716          59.90          High income
# 7             Antigua and Barbuda         ATG     16.447          63.40          High income
# ..                            ...         ...        ...            ...                  ...
# 190                        Tuvalu         TUV     30.963          58.27  Lower middle income
# 191  United States Virgin Islands         VIR     15.723          83.56          High income
# 192             Wallis and Futuna         WLF     17.363          87.29          High income
# 196                       Lesotho         LSO     24.148          72.07  Upper middle income
# 199                        Guinea         GIN     20.650          66.04  Upper middle income

print(df[df["IncomeGroup"]== "High income"])

#                      CountryName CountryCode  BirthRate  InternetUsers  IncomeGroup
# 0                           Aruba         ABW     10.244          78.90  High income
# 4            United Arab Emirates         ARE     11.044          88.00  High income
# 5                       Argentina         ARG     17.716          59.90  High income
# 7             Antigua and Barbuda         ATG     16.447          63.40  High income
# 8                       Australia         AUS     13.200          83.00  High income
# ..                            ...         ...        ...            ...          ...
# 168                      Guernsey         GGY     43.741          90.35  High income
# 175                         Nauru         NRU      9.260          93.08  High income
# 186                   Timor-Leste         TLS     37.962          82.14  High income
# 191  United States Virgin Islands         VIR     15.723          83.56  High income
# 192             Wallis and Futuna         WLF     17.363          87.29  High income

# [64 rows x 5 columns]

#New column based on BirthRate and custom values
# ==================================================

def get_rate(rate):
    if rate < 30:
        return "Less"
    elif rate <= 60:
        return "Average"
    else:
        return "High"

df["dfRate"] = df["BirthRate"].apply(get_rate)

print(df)
#             CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup   dfRate
# 0                   Aruba         ABW     10.244          78.90          High income     Less
# 1             Afghanistan         AFG     35.253           5.90           Low income  Average
# 2                  Angola         AGO     45.985          19.10  Upper middle income  Average
# 3                 Albania         ALB     12.877          57.20  Upper middle income     Less
# 4    United Arab Emirates         ARE     11.044          88.00          High income     Less
# ..                    ...         ...        ...            ...                  ...      ...
# 195      Papua New Guinea         PNG     16.493          12.01           Low income     Less
# 196               Lesotho         LSO     24.148          72.07  Upper middle income     Less
# 197               Liberia         LBR     13.465          43.66  Lower middle income     Less
# 198                 Gabon         GAB     31.026          35.93           Low income  Average
# 199                Guinea         GIN     20.650          66.04  Upper middle income     Less

# [200 rows x 6 columns]

print(df)

def get_bpl(inc):
    if inc == "High income":
        return "Above BPL"
    elif inc == "Upper middle income":
        return "Upper BPL"
    elif inc == "Lower middle income":
        return "Lower BPL"
    elif inc == "Low income":
        return "Under BPL"
    else:
        return "Nothing"

df["BPL"] = df["IncomeGroup"].apply(get_bpl)
print(df)
#               CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup   dfRate        BPL
# 0                   Aruba         ABW     10.244          78.90          High income     Less  Above BPL
# 1             Afghanistan         AFG     35.253           5.90           Low income  Average  Under BPL
# 2                  Angola         AGO     45.985          19.10  Upper middle income  Average  Upper BPL
# 3                 Albania         ALB     12.877          57.20  Upper middle income     Less  Upper BPL
# 4    United Arab Emirates         ARE     11.044          88.00          High income     Less  Above BPL
# ..                    ...         ...        ...            ...                  ...      ...        ...
# 195      Papua New Guinea         PNG     16.493          12.01           Low income     Less  Under BPL
# 196               Lesotho         LSO     24.148          72.07  Upper middle income     Less  Upper BPL
# 197               Liberia         LBR     13.465          43.66  Lower middle income     Less  Lower BPL
# 198                 Gabon         GAB     31.026          35.93           Low income  Average  Under BPL
# 199                Guinea         GIN     20.650          66.04  Upper middle income     Less  Upper BPL

# [200 rows x 7 columns]

df["CheckBPL"] = df["BPL"].apply(lambda x: "Yes" if x == "Above BPL" else "No")
print(df)
#    CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup   dfRate        BPL CheckBPL
# 0                   Aruba         ABW     10.244          78.90          High income     Less  Above BPL      Yes
# 1             Afghanistan         AFG     35.253           5.90           Low income  Average  Under BPL       No
# 2                  Angola         AGO     45.985          19.10  Upper middle income  Average  Upper BPL       No
# 3                 Albania         ALB     12.877          57.20  Upper middle income     Less  Upper BPL       No
# 4    United Arab Emirates         ARE     11.044          88.00          High income     Less  Above BPL      Yes
# ..                    ...         ...        ...            ...                  ...      ...        ...      ...
# 195      Papua New Guinea         PNG     16.493          12.01           Low income     Less  Under BPL       No
# 196               Lesotho         LSO     24.148          72.07  Upper middle income     Less  Upper BPL       No
# 197               Liberia         LBR     13.465          43.66  Lower middle income     Less  Lower BPL       No
# 198                 Gabon         GAB     31.026          35.93           Low income  Average  Under BPL       No
# 199                Guinea         GIN     20.650          66.04  Upper middle income     Less  Upper BPL       No

# [200 rows x 8 columns]

df["mulCondition"] = df.apply(lambda row: "Yes" if row["CheckBPL"] == "Yes" and row["dfRate"] == "Less" else "No", axis=1)
print(df)


print(df[(df.BirthRate >40) & (df.InternetUsers >50)])
print(df)
#               CountryName CountryCode  BirthRate  InternetUsers          IncomeGroup   dfRate        BPL CheckBPL mulCondition
# 0                   Aruba         ABW     10.244          78.90          High income     Less  Above BPL      Yes          Yes
# 1             Afghanistan         AFG     35.253           5.90           Low income  Average  Under BPL       No           No
# 2                  Angola         AGO     45.985          19.10  Upper middle income  Average  Upper BPL       No           No
# 3                 Albania         ALB     12.877          57.20  Upper middle income     Less  Upper BPL       No           No
# 4    United Arab Emirates         ARE     11.044          88.00          High income     Less  Above BPL      Yes          Yes
# ..                    ...         ...        ...            ...                  ...      ...        ...      ...          ...
# 195      Papua New Guinea         PNG     16.493          12.01           Low income     Less  Under BPL       No           No
# 196               Lesotho         LSO     24.148          72.07  Upper middle income     Less  Upper BPL       No           No
# 197               Liberia         LBR     13.465          43.66  Lower middle income     Less  Lower BPL       No           No
# 198                 Gabon         GAB     31.026          35.93           Low income  Average  Under BPL       No           No
# 199                Guinea         GIN     20.650          66.04  Upper middle income     Less  Upper BPL       No           No

# [200 rows x 9 columns]

print(df["IncomeGroup"].unique())
# ['High income', 'Low income', 'Upper middle income', 'Lower middle income']
# Length: 4, dtype: str

print(df["IncomeGroup"].value_counts())
# IncomeGroup
# High income            64
# Upper middle income    51
# Lower middle income    46
# Low income             39
# Name: count, dtype: int64

print(df["BPL"].unique())
# ['Above BPL', 'Under BPL', 'Upper BPL', 'Lower BPL']
print(df["BPL"].value_counts())
# BPL
# Above BPL    64
# Upper BPL    51
# Lower BPL    46
# Under BPL    39
# Name: count, dtype: int64

print(df["BPL"].nunique())
#4
print(df.nunique())
# CountryName      200
# CountryCode      200
# BirthRate        117
# InternetUsers    135
# IncomeGroup        4
# dfRate             2
# BPL                4
# CheckBPL           2
# mulCondition       2
# dtype: int64