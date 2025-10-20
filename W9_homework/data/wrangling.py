import pandas as pd

# Load the CSV
df = pd.read_csv('/Users/alicesolomon/Desktop/FIT3179/git/FIT3179/W9_homework/data/reason_v2.csv')

# Extract the year from the TIME_PERIOD column
df['year'] = pd.to_datetime(df['TIME_PERIOD']).dt.year

# Group by 'year' and 'reason' and sum 'OBS_VALUE'
result = df.groupby(['year', 'Reason for journey'], as_index=False)['OBS_VALUE'].sum()

# Optional: save the result to a new CSV
result.to_csv('reason_v2_processed.csv', index=False)

print(result)
