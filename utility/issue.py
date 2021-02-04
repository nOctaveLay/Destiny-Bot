import requests
import json
import os.path
from datetime import datetime,date,timedelta

__all__ = ['update_issue','read_issue','save_issue']

def update_issue():
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
            string_format = {"날짜": dict_date, "시간":update_time_iso, "제목": dict_title}
            result_data.append(string_format)
    result_data = sorted(result_data,key = lambda issue: issue['날짜'])
    return result_data

def read_issue(file_name):
    if os.path.isfile(file_name):
        with open(file_name,'r',encoding = 'utf-8') as f:
            issue_data = f.read()
        issue_data= json.loads(issue_data)
    else:
        issue_data = update_issue()
        save_issue(file_name,issue_data)
    return issue_data

def save_issue(file_name,save_data):
    json_list = json.dumps(save_data)
    with open(file_name,'w',encoding = 'utf-8') as f:
        f.write(json_list)

def show_issue():
    file_name = "_issue.txt"
    today_datetime = datetime.today()
    issue_raw_data = read_issue(file_name)
    issue_raw_data = sorted(issue_raw_data,key = lambda issue: (issue['날짜'],issue['시간']))
    last_date = issue_raw_data[0]['날짜'].split('-')
    last_updated_hour = issue_raw_data[0]['시간'].split(':')
    
    last_datetime = datetime(year = int(last_date[0]), month = int(last_date[1]), day = int(last_date[2]), hour = int(last_updated_hour[0]), minute = int(last_updated_hour[1]),second = int(last_updated_hour[2]))
    
    diff_timedelta = today_datetime - last_datetime
    if diff_timedelta.days >0 or (diff_timedelta.days == 0 and diff_timedelta.hour > 1):
        issue_data = update_issue()
        save_issue(file_name,issue_data)
    else:
        issue_data = issue_raw_data
    result_string = ''
    for index in range(1,len(issue_data)+1):
        result_string += f'{index} - {issue_data[index-1]["제목"]}\n'
    return result_string