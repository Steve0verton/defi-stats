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

# Keep columns needed
df = df[df.columns[df.columns.isin(['id','name','address','symbol','url','description','chain','logo','audits','gecko_id','cmcId','category','chains','module','twitter','audit_links','oracles','language',',lug','tvl','change_1h','change_1d','change_7d','staking','fdv','mcap'])]]

# Debug output to print list of columns in flattened JSON
for col in df.columns:
    print(col)

# Debug output
print(df)

# Save as CSV file
df.to_csv('defi-protocols.csv')

