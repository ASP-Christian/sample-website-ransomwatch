import os
import json

# Create a new directory
new_dir = 'my_new_directory'
os.makedirs(new_dir, exist_ok=True)

# Create data for the JSON file
data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'age': 30
}

# Write data to a JSON file inside the new directory
json_file_path = os.path.join(new_dir, 'data.json')
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Created directory '{new_dir}' with JSON file '{json_file_path}'")
