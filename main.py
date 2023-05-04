import json

class schema:
    def __init__ (self):
        self.tableNames = []


with open('./spider-data/tables.json', 'r') as f:
  data = json.load(f)

schemas = []

for idx, iSchema in enumerate(data):
    test = schema()
    for columnName in iSchema['table_names']:
        test.tableNames.append(columnName)
    print("Schema", idx, ":", test.tableNames)
    schemas.append(test)

print("Hello TextToSQL")