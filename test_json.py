
import json
from datetime import datetime;
issue_data = dict()
today = datetime.today().strftime('%Y-%m-%d')
issue_name = 'issue'
if today not in issue_data:
    issue_data[today] = [issue_name]
else:
    issue_data[today].append(issue_name)
jsonString = json.dumps(issue_data,indent=4)
print(jsonString)
