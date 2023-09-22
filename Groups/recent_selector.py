import json
import datetime

# Calculate the start and end date of the current week
today = datetime.date.today()
start_of_week = today - datetime.timedelta(days=today.weekday())
end_of_week = start_of_week + datetime.timedelta(days=6)

# Load data from data_post.json
with open('Groups/Overall_data/data_post.json', 'r') as data_file:
    data = json.load(data_file)

# Convert date strings to datetime objects for comparison (strip leading/trailing spaces)
data = [
    entry for entry in data if
    start_of_week <= datetime.datetime.strptime(entry['data_date'].strip(), "%Y-%m-%d").date() <= end_of_week
]

# Save the filtered data to recent_data.json
with open('Groups/Overall_data/recent_data.json', 'w') as recent_data_file:
    json.dump(data, recent_data_file, indent=4)
