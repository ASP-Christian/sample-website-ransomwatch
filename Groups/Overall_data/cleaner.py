import json

# Read data from the data_post.json file with the appropriate encoding
with open('data_post.json', 'r', encoding='utf-8') as data_file:
    data = json.load(data_file)

# Create a dictionary to store unique companies
unique_companies = {}

# Iterate through the data and add unique companies to the dictionary
for item in data:
    company = item["company"]
    if company not in unique_companies:
        unique_companies[company] = item

# Convert the dictionary values (unique items) back to a list
cleaned_data = list(unique_companies.values())

# Save the cleaned data to cleaneddata_post.json
with open('cleaneddata_post.json', 'w', encoding='utf-8') as cleaned_data_file:
    json.dump(cleaned_data, cleaned_data_file, indent=4)

print("Duplicates removed and cleaned data saved to cleaneddata_post.json.")
