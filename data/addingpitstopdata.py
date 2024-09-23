import pandas as pd

# Load the CSV files
results = pd.read_csv('results.csv')
pit_stops = pd.read_csv('pit_stops.csv')

# For each raceId and driverId combo, find the maximum 'stop' value (the number of pit stops)
max_pit_stops = pit_stops.groupby(['raceId', 'driverId'])['stop'].max().reset_index()

print(max_pit_stops)

# Merge the maximum pit stop values into results.csv on raceId and driverId
results = pd.merge(results, max_pit_stops, on=['raceId', 'driverId'], how='left')

# Add a new column 'number_of_pit_stops' and fill missing values with 0 (for drivers without pit stops)
results['number_of_pit_stops'] = results['stop'].fillna(0)

# Save the updated results.csv with the new column 'number_of_pit_stops'
results.to_csv('results_with_pit_stops.csv', index=False)

# Output the first few rows of the updated dataframe to verify
print(results.head())