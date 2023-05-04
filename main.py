import json

with open('./spider-data/tables.json', 'r') as f:
  data = json.load(f)

for columnName in data[0]['column_names']:
  print(columnName[1])

print("Hello TextToSQL")