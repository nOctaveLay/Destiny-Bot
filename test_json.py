import requests
import json
import os.path
from datetime import datetime,date,timedelta



def update():
    auth = {'User-Agent':'nOctaveLay'}
    res = requests.get("https://api.github.com/repos/nOctaveLay/Destiny-Bot/issues?state=closed",headers = auth)
    issue_data = res.json()
    result_data = []
    today = date.today()
    today_datetime = datetime.today()
    update_time_iso = datetime.isoformat(today_datetime,timespec ='seconds')
    update_time_iso = update_time_iso[update_time_iso.index('T')+1:]
    result_data.append({"시간":update_time_iso})
    time_delta = timedelta(days = 8)
    today_delta = today - time_delta

    # now_time = time.gmtime()
    # now_time.tm_hour = now_time.tm_hour += 9

    for data in issue_data:
        end_time = data['closed_at']
        end_time_iso = end_time[:end_time.index('T')]
        end_time = date.fromisoformat(end_time_iso)
        if end_time <= today and end_time > today_delta:
            dict_date,dict_title = end_time_iso,data['title']
            string_format = {"날짜": dict_date, "제목": dict_title}
            result_data.append(string_format)
    return result_data

today = date.today()
today_datetime = datetime.today()
file_name = 'issue_name.txt'
time_delta = timedelta(days = 8)
search_range = today - time_delta
if os.path.isfile(file_name):
    with open(file_name,'r',encoding = 'utf-8') as f:
        issue_data = f.read()
issue_convert_json = json.loads(issue_data)
if '시간' in issue_convert_json[0]:
    text_time = issue_convert_json[0]['시간']
    text_time = text_time.split(":")
else: text_time = today

issue_date = date.fromisoformat(issue_convert_json[1]['날짜'])
if issue_date < today or text_time[0] < today_datetime.hour-1:
    issue_data = update()

json_list = json.dumps(issue_data)
with open('issue_name.txt','w',encoding = 'utf-8') as f:
    f.write(json_list)
