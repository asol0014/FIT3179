import pandas as pd

# Load the data from the specified CSV file
file_name = '/Users/alicesolomon/Desktop/FIT3179/git/FIT3179/W9_homework/data/country_passengers_from.csv'
df = pd.read_csv(file_name)

df['OBS_VALUE'] = pd.to_numeric(df['OBS_VALUE'], errors='coerce')


df_filtered = df[df['CAT_TRAVELLER'] == 6].copy()

countries_to_exclude = ['other', 'total', 'not stated', 'uk, cis & iom']
mask = ~df_filtered['Country of Stay/Residence'].astype(str).str.lower().str.contains('|'.join(countries_to_exclude), regex=True, na=False)
df_filtered = df_filtered[mask].copy()

time_periods = df_filtered['TIME_PERIOD'].astype(str).str.split('-')
df_filtered['Year'] = time_periods.str[0]
df_filtered['Month'] = time_periods.str[1]

df_grouped = df_filtered.groupby(['Year', 'Country of Stay/Residence', 'Origin'])['OBS_VALUE'].sum().reset_index()

df_grouped = df_grouped.rename(columns={'OBS_VALUE': 'Total_OBS_VALUE'})

output_file = 'country_passengers_from_processed.csv'
df_grouped.to_csv(output_file, index=False)

# Display the final results
print(df_grouped.head())
