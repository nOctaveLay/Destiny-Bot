__all__ = ['init_raid','print_no_named','show_challenge']
from collections import defaultdict
from datetime import datetime, date, timedelta
import json
import os
def init_raid():
    raid_list = ['마지막 소원', '구원의 정원','딥스톤 무덤']
    return raid_list

def print_no_named():
    result_string = f"수호자님, 음... 이 보스는 역할 분배를 하지 않아도 되는 보스인 거 같아요."
    return result_string

def show_challenge():
    file_name = "./data/challenge.txt"
    raid_keys = init_raid()
    raid_list = list()
    if os.path.isfile(file_name):
        with open(file_name,'r',encoding = 'utf-8') as f:
            raid_list = f.read()
        raid_list = json.loads(raid_list)
    else:
        for key in raid_keys:
            raid_challenge = dict()
            raid_challenge['title'] = key
            raid_challenge['date'] = date.isoformat(datetime.today())
            raid_challenge['challenge'] = 1
            raid_list.append(raid_challenge)
        save_list_into_json(file_name,raid_list)
    result_string = '\n이번 레이드의 챌린지를 보여드릴게요.\n'
    for index,raid_challenge in enumerate(raid_list):
        raid_challenge = update_challenge(raid_challenge)
        result_string += f'{raid_challenge["title"]}: {raid_challenge["challenge"]}네임드 \n'
        raid_list[index] = raid_challenge
    save_list_into_json(file_name,raid_list)
    return result_string

def update_challenge(raid_challenge):
    today_date = datetime.today()
    written_date = datetime.fromisoformat(raid_challenge['date'])
    week = (today_date-written_date).days // 7
        # time_check = timedelta(days=1)
        # while (written_date == today_date):
        #     if written_date.weekday() == 1:
        #         week = 1
        #         written_date += time_check
    if raid_challenge['title'] == '마지막 소원': num = 5
    else: num = 4
    raid_challenge["challenge"] = (int(raid_challenge["challenge"])-1+week)%num+1
    raid_challenge["date"] = date.isoformat(today_date)
    return raid_challenge

def save_list_into_json(file_name,save_list):
    with open(file_name,'w',encoding = 'utf-8') as f:
        dumps = json.dumps(save_list)
        f.write(dumps)

print(show_challenge())