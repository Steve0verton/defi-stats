import json
import csv
import urllib.request
import pandas

# defillama API endpoint
url = "https://api.llama.fi/protocols"

# Extract JSON response payload
with urllib.request.urlopen(url) as url:
    json_data = json.loads(url.read().decode())

# Flatten JSON to CSV
# TODO: select certain JSON fields and filter/group by network
df = pandas.json_normalize(json_data, max_level=1)

# Debug output
print(df)

# Save as CSV file
df.to_csv('defi-protocols.csv')
