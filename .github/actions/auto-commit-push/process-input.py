import sys
import json


data = json.loads(sys.argv[1])
files = data['move to base folder output']
for file in files:
  print(file)
