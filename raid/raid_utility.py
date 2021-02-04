__all__ = ['init_raid','print_no_named']
from collections import defaultdict
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
    if os.path.isfile(file_name):
        with open(file_name,'r',encoding = 'utf-8') as f:
            raid_challenge = f.read()
        raid_challenge = json.loads(raid_challenge)
    else:
        raid_keys = init_raid()
        raid_challenge = dict.fromkeys(raid_keys, 1)
        with open(file_name,'w',encoding = 'utf-8') as f:
            dumps = json.dumps(raid_challenge)
            f.write(dumps)
    return raid_challenge
