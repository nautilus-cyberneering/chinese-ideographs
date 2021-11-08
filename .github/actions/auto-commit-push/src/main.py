import os
import json

data = json.loads(os.environ["INPUT_JOB_STATE"])
files = data['move to base folder output']
for file in files:
    print("File to commit: "+file)
