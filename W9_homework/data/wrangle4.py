import pandas as pd

# Load the CSV files
flights_df = pd.read_csv('/Users/alicesolomon/Desktop/FIT3179/git/FIT3179/W9_homework/data/aircraft.csv')
pax_df = pd.read_csv('/Users/alicesolomon/Desktop/FIT3179/git/FIT3179/W9_homework/data/passengers.csv')

# Standardize airport column names and make them lowercase for case-insensitive join
flights_df['airport_lower'] = flights_df['airport'].str.lower()
pax_df['airport_lower'] = pax_df['AIRPORT'].str.lower()

# Merge the dataframes on airport (case-insensitive), Year, and Month
merged_df = pd.merge(
    flights_df,
    pax_df,
    left_on=['airport_lower', 'Year', 'Month'],
    right_on=['airport_lower', 'Year', 'Month'],
    how='inner',
    suffixes=('_flight', '_pax')
)

# Drop the helper column
merged_df.drop(columns=['airport_lower'], inplace=True)

merged_df['airport'] = merged_df['airport'].str.title()
merged_df['AIRPORT'] = merged_df['AIRPORT'].str.title()

# Export to a new CSV
merged_df.to_csv("pax_flight_corr.csv", index=False)

print("Merged CSV saved as pax_flight_corr.csv")
