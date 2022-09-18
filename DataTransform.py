# Import of necessary modules
import datetime

import pandas as pd

# Read the Excel into a df
df = (
    pd.concat(
        pd.read_excel(
            "1990-2021_PC-by-country_EUEFTAUK - ACEA.xlsx",
            sheet_name=None,
            header=5,
        ),
        ignore_index=True,
    )
    .drop_duplicates()
    .reset_index(drop=True)
)

# Clean & Transform df to country/region grouped data
df.rename(columns={df.columns[0]: "Country/Region"}, inplace=True)
df = df.drop(df.filter(regex="FY").columns, axis=1)
df = df.groupby("Country/Region", as_index=False, sort=False).first()

# check df
# print(df)

countries = [
    "Austria",
    "Belgium",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland" "France",
    "Germany",
    "Greece",
    "Hungary",
    "Ireland",
    "Italy",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Netherlands",
    "Poland",
    "Portugal",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "United Kingdom",
    "Iceland",
    "Norway",
    "Switzerland",
]

# create df focused on countries only
df_countries = df[df["Country/Region"].isin(countries)]

# Check the countries df
# print(df_countries)

# fix the names of dates columns to just Month-Year
df_countries.columns = [
    col.strftime("%b-%Y") if (isinstance(col, datetime.date)) else col
    for col in df_countries.columns
]
# check the columns name
print(df_countries.columns)

# Export the data to CSV to make into Bar Chart Race :)
df_countries.to_csv("ACEA_CleanedData.csv", index=False)
