import pandas as pd

df = pd.read_csv('country_passengers_from.csv')

grouping_columns = ['Origin', 'Country of Stay/Residence', 'TIME_PERIOD']

grouped_data = df.groupby(grouping_columns)['OBS_VALUE'].sum().reset_index()

# Rename the summed column for clarity
grouped_data = grouped_data.rename(columns={'OBS_VALUE': 'TOTAL_OBS_VALUE'})

# Export the result to the specified CSV file
grouped_data.to_csv('country_passengers_from_clean.csv', index=False)

print("Grouping complete. The summarized data has been saved to 'country_passengers_from_clean.csv'.")
print("\n--- First 5 rows of the exported data ---")
print(grouped_data.head())