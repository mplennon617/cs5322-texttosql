import json

class schema:
    def __init__ (self, id):
        self.id = id
        self.tableNames = []
        self.columnNames = []
        self.columnAtributes = []


# Loading Spider Data

with open('./spider-data/tables.json', 'r') as f:
  schemaDoc = json.load(f)

with open('./spider-data/train_spider.json', 'r') as f:
  queryDoc = json.load(f)

schemas = {}

for idx, iSchema in enumerate(schemaDoc):
    dbid = iSchema['db_id']
    test = schema(dbid)
    for columnName in iSchema['table_names_original']:
      test.tableNames.append(columnName)
    for columnName in iSchema['column_names_original']:
      test.columnNames.append(columnName[1])
      test.columnAtributes.append(columnName[0])
    #print("Schema", idx, ":", test.id, ":", test.tableNames)
    #print("Columns:", test.columnNames)
    #print("Atributes:", test.columnAtributes)
    #print()
    schemas[dbid] = test

for idx, iquery in enumerate(queryDoc):
   # Initialize a blank array with the length of the number of tables
   tablesArray = [0] * len(schemas[iquery['db_id']].tableNames)
   columnsArray = [0] * len(schemas[iquery['db_id']].columnNames)
   # Get all the tokens from teh particular query we are looking at
   queryTokens = iquery['query_toks_no_value']

    # TODO: Use spacy to tag all table names using named entity recognition (NER).

   # Search through all the tokens in the given query
   for idx, queryToken in enumerate(queryTokens):
      # Only look at tokens that come after the word "from," since those are the table names
      if (idx > 0) & (queryTokens[idx - 1].lower() == "from") | (queryTokens[idx - 1].lower() == "join"):
        # Search through all of the table names in the database we are looking at
        for jdx, tableName in enumerate(schemas[iquery['db_id']].tableNames):
           # If the table names match, indicate it in tablesArray
           if tableName.lower() == queryToken.lower():
              tablesArray[jdx] = 1
      else:
         # Search through all of the column names in the database we are looking at
         for jdx, tableName in enumerate(schemas[iquery['db_id']].columnNames):
           # If the table names match, indicate it in tablesArray
           if tableName.lower() == queryToken.lower():
              columnsArray[jdx] = 1
   print(tablesArray, columnsArray)
   #print(schemas[iquery['db_id']].id)
   #print(iquery['query_toks'])

print("Hello TextToSQL")