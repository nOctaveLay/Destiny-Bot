__all__ = ['init_raid','print_no_named','show_challenge']
from collections import defaultdict
from datetime import datetime, date
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
        with open(file_name,'w',encoding = 'utf-8') as f:
            dumps = json.dumps(raid_list)
            f.write(dumps)
    result_string = '\n이번 레이드의 챌린지를 보여드릴게요.\n'
    for raid_challenge in raid_list:
        result_string += f'{raid_challenge["title"]}: {raid_challenge["challenge"]}네임드 \n'
    return result_string

def week_update(date):
    today_date = datetime.today()