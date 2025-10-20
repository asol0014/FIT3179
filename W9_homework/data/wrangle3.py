import pandas as pd
import io

df = pd.read_csv('/Users/alicesolomon/Desktop/FIT3179/git/FIT3179/W9_homework/data/INT_passengers.csv')

# 

# 1. Convert 'Year' column to a numeric type (in case it was read as a string)
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# 2. Filter the DataFrame
# The condition df['Year'] >= 1990 creates a boolean Series (True/False).
# Applying this Series to the DataFrame selects only the rows where the condition is True.
df_filtered = df[df['Year'] >= 1990].copy()

print("\nFiltered DataFrame Head (Year >= 1990):")
print(df_filtered.head())

output_file = 'INT_passengers_processed.csv'
df_filtered.to_csv(output_file, index=False)
