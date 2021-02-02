import requests
import json
import os.path
from datetime import datetime,date,timedelta

__all__ = ['update','issue_read','issue_save']

def update():
    auth = {'User-Agent':'nOctaveLay'}
    res = requests.get("https://api.github.com/repos/nOctaveLay/Destiny-Bot/issues?state=closed",headers = auth)
    issue_data = res.json()
    result_data = []
    today = date.today()
    today_datetime = datetime.today()
    update_time_iso = datetime.isoformat(today_datetime,timespec ='seconds')
    update_time_iso = update_time_iso[update_time_iso.index('T')+1:]
    time_delta = timedelta(days = 8)
    today_delta = today - time_delta

    for data in issue_data:
        end_time = data['closed_at']
        end_time_iso = end_time[:end_time.index('T')]
        end_time = date.fromisoformat(end_time_iso)
        if end_time <= today and end_time > today_delta:
            dict_date,dict_title = end_time_iso,data['title']
            string_format = {"날짜": dict_date, "제목": dict_title}
            result_data.append(string_format)
    result_data = sorted(result_data,key = lambda issue: issue['날짜'])
    result_data.append({"시간":update_time_iso})
    return result_data

def issue_read():
    file_name = 'issue_name.txt'
    if os.path.isfile(file_name):
        with open(file_name,'r',encoding = 'utf-8') as f:
            issue_data = f.read()
        issue_data= json.loads(issue_data)
        today = date.today()
        today_datetime = datetime.today()
        issue_convert_json = issue_read()
        if '시간' in issue_convert_json[0]:
            text_time = issue_convert_json[0]['시간']
            text_time = text_time.split(":")
            text_time = text_time[0]
        else: text_time = today_datetime.hour
        issue_date = date.fromisoformat(issue_convert_json[1]['날짜'])
        if issue_date < today or text_time < today_datetime.hour-1:
            issue_data = update()
        issue_save(issue_data)
    else:
        issue_data = update()
    return issue_data

def issue_save(save_data):
    file_name = 'issue_name.txt'
    json_list = json.dumps(save_data)
    with open(file_name,'w',encoding = 'utf-8') as f:
        f.write(json_list)