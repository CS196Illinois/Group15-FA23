import json
import os

unique_country_codes = set()

# Iterate through all .ndjson files in the Data directory
for filename in os.listdir('Data'):
    if filename.endswith('.ndjson'):
        with open(os.path.join('Data', filename), 'r') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    country_code = data.get('countrycode')
                    if country_code is not None:
                        unique_country_codes.add(country_code)
                except json.JSONDecodeError:
                    print(f"Error parsing JSON in file {filename}")

# Create a new .txt file to store unique country codes
output_file = 'Unique_Country_Codes.txt'

# Write the unique country codes to the output file
with open(output_file, 'w') as file:
    for code in unique_country_codes:
        file.write(code + '\n')

print(f"Unique country codes have been written to {output_file}")