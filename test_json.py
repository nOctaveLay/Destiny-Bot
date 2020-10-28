import requests
import json
import os.path
from datetime import datetime,date,timedelta


auth = {'User-Agent':'nOctaveLay'}
today = date.today()
file_name = 'issue_name.txt'
time_delta = timedelta(days = 8)
search_range = today - time_delta
if os.path.isfile(file_name):
    with open(file_name,'r',encoding = 'utf-8') as f:
        issue_data = f.read()
issue_convert_json = json.loads(issue_data)

# max_time = search_range
# file_issue_data = list()
# for issue_element in issue_convert_json:
#     issue_date = date.fromisoformat(issue_element['날짜'])
#     if max_time < issue_date:
#         max_time = issue_date  
res = requests.get("https://api.github.com/repos/nOctaveLay/Destiny-Bot/issues?state=closed",headers = auth)
issue_data = res.json()
issue_list = list()
for issue_element in issue_data:
    issue_end_time_iso = issue_element['closed_at']
    T_index = issue_end_time_iso.find('T')
    issue_end_time_iso = issue_end_time_iso[:T_index]
    issue_end_time = date.fromisoformat(issue_end_time_iso)
    if issue_end_time <= today and search_range < issue_end_time:
        title = issue_element['title']
        string_format = {"날짜": issue_end_time_iso, "제목": title}
        issue_list.append(string_format)
issue_list = sorted(issue_list,key = lambda issue:issue[0].values)
print(issue_list)
json_list = json.dumps(issue_list)
with open('issue_name.txt','w',encoding = 'utf-8') as f:
    f.write(json_list)

# today = datetime.today().strftime('%Y-%m-%d')
# issue_name = 'issue'
# if today not in issue_data:
#     issue_data[today] = [issue_name]
# else:
#     issue_data[today].append(issue_name)
# jsonString = json.dumps(issue_data,indent=4)
