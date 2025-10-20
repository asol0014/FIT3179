import pandas as pd

# Load the CSV
df = pd.read_csv('/Users/alicesolomon/Desktop/FIT3179/git/FIT3179/W9_homework/data/reason_v2.csv')

# Remove rows where 'Reason for journey' contains 'total' (case-insensitive)
df = df[~df['Reason for journey'].str.contains('total', case=False, na=False)]

# Extract the year from the TIME_PERIOD column
df['year'] = pd.to_datetime(df['TIME_PERIOD']).dt.year

# Group by 'year' and 'Reason for journey', summing 'OBS_VALUE'
df_grouped = df.groupby(['year', 'Reason for journey'], as_index=False)['OBS_VALUE'].sum()

# Calculate total per year
df_grouped['total_per_year'] = df_grouped.groupby('year')['OBS_VALUE'].transform('sum')

# Calculate percentage and round to nearest tenth
df_grouped['percentage'] = round((df_grouped['OBS_VALUE'] / df_grouped['total_per_year']) * 100, 1)

# Optional: drop the total_per_year column if not needed
df_grouped = df_grouped.drop(columns='total_per_year')

# Save to a new CSV
df_grouped.to_csv('reason_v2_grouped_with_percentage.csv', index=False)

print(df_grouped)
