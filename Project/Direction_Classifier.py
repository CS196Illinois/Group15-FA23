import json

# Desired drawing types
drawing_types = ["circle", "triangle"]

def calculate_winding_number(x, y):
    n = len(x)
    winding_number = 0

    for i in range(n):
        x1, y1 = x[i], y[i]
        x2, y2 = x[(i + 1) % n], y[(i + 1) % n]

        winding_number += (x2 - x1) * (y2 + y1)

    if winding_number > 0:
        return "Counterclockwise"
    elif winding_number < 0:
        return "Clockwise"
    else:
        return "Undefined (not a closed curve)"

# Dictionary to store counts for each drawing type
total_counts = {}

# Dictionary to store the total undefined count for each shape
total_undefined_counts = {}

# Loop through the list of drawing types
for drawing_type in drawing_types:
    # Dictionary to store counts for each country for the current drawing type
    country_counts = {}

    # Process each country code
    with open('Project/Unique_Country_Codes.txt', 'r') as country_code_file:
        for line in country_code_file:
            country_code = line.strip()
            country_counts[country_code] = {
                "Clockwise": 0,
                "Counterclockwise": 0,
                "Undefined": 0  # New count for undefined drawings
            }

    # Open the .ndjson file for the current drawing type and process each JSON object
    with open(f'Data/{drawing_type}.ndjson', 'r') as file:
        for line in file:
            data = json.loads(line)
            drawing = data.get('drawing')
            country_code = data.get('countrycode')

            if drawing and country_code in country_counts:
                x = drawing[0][0]  # Extract x-coordinates
                y = drawing[0][1]  # Extract y-coordinates
                orientation = calculate_winding_number(x, y)
                if orientation == "Clockwise":
                    country_counts[country_code]["Clockwise"] += 1
                elif orientation == "Counterclockwise":
                    country_counts[country_code]["Counterclockwise"] += 1
                else:
                    country_counts[country_code]["Undefined"] += 1  # Increment undefined count for the country
                word = data.get('word')
                print(f"{word}, {country_code}, {orientation}")

    # Store the counts for the current drawing type in the total counts dictionary
    total_counts[drawing_type] = country_counts

# Print counts for each country for all drawing types
for drawing_type, country_counts in total_counts.items():
    for country_code, counts in country_counts.items():
        print(f"{drawing_type}, {country_code}, Clockwise: {counts['Clockwise']}, Counterclockwise: {counts['Counterclockwise']}, Undefined: {counts['Undefined']}")

# Calculate and print the total counts for each drawing type, including total undefined count
for drawing_type, country_counts in total_counts.items():
    total_clockwise = sum(counts['Clockwise'] for counts in country_counts.values())
    total_counterclockwise = sum(counts['Counterclockwise'] for counts in country_counts.values())
    total_undefined = sum(counts['Undefined'] for counts in country_counts.values())
    
    total_undefined_counts[drawing_type] = total_undefined  # Store total undefined count for each shape
    print(f"Drawing: {drawing_type}, Total Clockwise: {total_clockwise}, Total Counterclockwise: {total_counterclockwise}, Total Undefined: {total_undefined}")