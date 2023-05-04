import json

with open('./spider-data/tables.json', 'r') as f:
  data = json.load(f)

for idx, schema in enumerate(data):
    print("Schema", idx)
    for columnName in schema['table_names']:
        print(columnName)

print("Hello TextToSQL")