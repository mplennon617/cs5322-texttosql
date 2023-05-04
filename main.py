import json

class schema:
    def __init__ (self, id):
        self.id = id
        self.tableNames = []


with open('./spider-data/tables.json', 'r') as f:
  schemaDoc = json.load(f)

with open('./spider-data/train_spider.json', 'r') as f:
  queryDoc = json.load(f)

schemas = []

for idx, iSchema in enumerate(schemaDoc):
    test = schema(iSchema['db_id'])
    for columnName in iSchema['table_names']:
        test.tableNames.append(columnName)
    #print("Schema", idx, ":", test.id, ":", test.tableNames)
    schemas.append(test)

print("Hello TextToSQL")