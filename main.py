
import asyncio
from configparser import ConfigParser
import copy
import json
import os
import random
import re

import discord
from utility.issue import issue_read
from utility.init import *
from raid.dsc import *
from raid.gos import *
from raid.lw import *
from raid.no_named import *
from utility.utility import *
from utility.issue import *

client = discord.Client()
user = discord.User
config = ConfigParser()
config.read('./config.ini')
token = config['Default']['token']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # 봇 권한이 있는 곳에만 쓰도록 허락하자.
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel.name == "개발-테스트":
                await channel.send("으음... 여기가 어디죠?")

@client.event
async def on_message(message):

    #config 파일로 관리하는 방법 없을까 리스트도 너무 지저분한데...
    call_string = '사기라'

    activity_list,activity_text_dict = init_activity()
    raid_list,raid_text_dict = init_raid()
    raid_summary_list = ['마소','구정','딥스톤']

    error_message = '수호자님, 제가 알아들을 수 있는 말로 부탁드릴게요. **사기라 사용법**을 쓰면 제가 어떤 말을 알아듣는지 알 수 있을 거에요.'

    if message.author.bot:
        return

    if message.content.startswith(call_string):
        option = message.content.split(" ")
        option = option[1:]

        if len(option) == 0:
            num = 0
        else:
            num = init_num(option[-1])

        if num == -1 or num > 10:
            await message.channel.send(f"반복 횟수를 너무 많이 설정한 거 같아요, 수호자님. 어... 우선 1번만 돌릴게요")
            num = 1

        #이스터 에그    
        if '자발라' in option:
            await message.channel.send("여기서 그 파란 빡빡이를 왜 찾으시는 거죠?")

        elif len(option) == 0:
            await message.channel.send(f"왜 그러시죠? {message.author.name} 수호자님?")

        elif option[0] == '가위바위보' or option[0] == "감맘보":
            choose_one = random.choice(['가위','바위','보'])
            await message.channel.send(choose_one)

        elif option[0] == '랜덤':
            #랜덤
            if len(option) == 1 or (len(option) == 2 and num > 0 and '번' in option[1]):
                activity_num_dict = {key:0 for key in activity_list}
                for _ in range(num):
                    choosen_activity = choosen(activity_list)
                    activity_num_dict[choosen_activity] += 1
                text_dict = change_activity_text_dict(activity_num_dict)
                for x in text_dict:
                    await message.channel.send(x)

            #랜덤 레이드
            elif option[1] == '레이드':
                raid_num_dict = {key:0 for key in raid_list}
                for _ in range(num):
                    choosen_raid = choosen(raid_list)
                    raid_num_dict[choosen_raid] += 1
                text_dict = change_raid_text_dict(raid_num_dict)
                for x in text_dict:
                    await message.channel.send(x)
            else:
                await message.channel.send(error_message)

        elif option[0] in raid_summary_list:
            if option[0] == '마소':
                if len(option) == 1:
                    lw_string = print_lw_named()
                elif option[1] == '1넴' or option[1] == '1네임드':
                    lw_string = print_no_named()
                elif option[1] == '2넴' or option[1] == '2네임드':
                    lw_string = print_lw_sec_named()
                elif option[1] == '3넴' or option[1] == '3네임드':
                    lw_string = print_lw_third_named()
                elif option[1] == '4넴' or option[1] == '4네임드':
                    lw_string = print_lw_forth_named()
                elif option[1] == '5넴' or option[1] == '5네임드':
                    lw_string = print_no_named()
                elif option[1] == '6넴' or option[1] == '6네임드':
                    lw_string = print_no_named()
                else:
                    lw_string = "수호자님, 마지막 소원은 6보스로 되어 있는 거 아시죠? 아니면 명령어를 잘못 입력한 거 같은데... 확인해주세요."
                await message.channel.send(lw_string)
            elif option[0] == '구정':
                if len(option) == 1:
                    gos_string = print_gos_named()
                elif option[1] == '1넴' or option[1] == '1네임드':
                    gos_string = print_gos_first_named()
                elif option[1] == '2넴' or option[1] == '2네임드':
                    gos_string = print_gos_sec_named()
                elif option[1] == '3넴' or option[1] == '3네임드':
                    gos_string = print_gos_third_named()
                elif option[1] == '4넴' or option[1] == '4네임드':
                    gos_string = print_gos_forth_named()
                else:
                    gos_string = "수호자님, 구원의 정원은 보스가 총 4명 있는 거 아시죠? 아니면 명령어를 잘못 입력한 거 같은데... 확인해주세요."
                await message.channel.send(gos_string)
            
            else:
                if len(option) == 1:
                    dsc_string = print_dsc_named()
                elif option[1] == '1넴' or option[1] == '1네임드':
                    dsc_string = print_dsc_first_named()
                elif option[1] == '2넴' or option[1] == '2네임드':
                    dsc_string = print_dsc_sec_named()
                elif option[1] == '3넴' or option[1] == '3네임드':
                    dsc_string = print_no_named()
                elif option[1] == '4넴' or option[1] == '4네임드':
                    dsc_string = print_dsc_forth_named()
                else:
                    dsc_string = "수호자님, 딥스톤 무덤은 4명의 보스가 대기하고 있는 거 아시죠? 아니면 명령어를 잘못 입력한 거 같은데... 확인해주세요."
                await message.channel.send(dsc_string)
                
        elif option[0] == '사용법' or option[0] == 'help' or option[0] == '도움':
            use_string = usage()
            await message.channel.send(use_string)

        elif option[0] == '소라고동' or option[0] == '소라고둥':
            choose_one = random.choice(['그럼요. 물론이죠.','아니요.','음... 잘 모르겠네요. 오시리스에게 한 번 물어보죠...'])
            await message.channel.send(choose_one)

        #이스터 에그
        elif option[0] == '자폭해':
            await message.channel.send(f"{message.author.name} 수호자님? 어떻게... 저를 죽이려 하실 수가 있죠?")

        elif option[0] == '안녕':
            await message.channel.send(f"{message.author.name} 수호자님, 안녕하세요?")    
        
                
        # elif option[0] == '오늘': #오늘
        #     if len(option) < 1:
        #         await message.channel.send("봇을 사용할 수 없습니다, 명령어가 없는게 아닐지?")

        #     elif len(option) == 1:
        #         await message.channel.send("오늘 돌아야 하는 것에 대해서 말씀드릴게요.")
        #         today_count = additive_option(count_activity)
        #         today_all_dict = multiple_activity(random_activity,today_count)
        #         for printer_ in print_random_dict(today_all_dict):
        #             await message.channel.send(printer_) 
            
        #     elif option[1] == '하드':
        #         mode = random.randint(0,1)
        #         if mode == 0:
        #             option_set = ['easy','hard']
        #         else:
        #             option_set = ['hard','easy']
        #         today_count = additive_option(count_activity, option = option_set[0])
        #         today_all_dict = multiple_activity(random_activity,today_count,option = option_set[1])
        #         for printer_ in print_random_dict(today_all_dict):
        #             await message.channel.send(printer_)
        #     elif option[1] == '라이트':
        #         today_count = additive_option(count_activity, option = 'easy')
        #         today_all_dict = multiple_activity(random_activity,today_count)
        #         for printer_ in print_random_dict(today_all_dict):
        #             await message.channel.send(printer_)

        #     elif option[1] == "공격전":
        #         if len(option) == 3:
        #             strike_num = additive_option(count_strike,option[2])
        #         else:
        #             strike_num = count_strike()
        #         string = string_format('공격전',strike_num)
        #         await message.channel.send(string)

        #     elif option[1] == "레이드":
        #         if len(option) == 3:
        #             raid_num = additive_option(count_activity,option[2]) 
        #         else :
        #             raid_num = count_activity()
        #         string = string_format('레이드',raid_num)
        #         await message.channel.send(string)
        #         if len(option) > 3 or (len(option) == 3 and (option[2] != '라이트' and option[2] != '하드')):
        #             raid_dict = multiple_activity(random_raid,raid_num)
        #             for key, value in raid_dict.items():
        #                 string = print_raid(key)
        #                 string = string + f" {str(value)}번 정도면 충분할 거 같아요."
        #                 await message.channel.send(string)

        #     elif option[1] == "시장" or option[1].startswith("시련"):
        #         if len(option) >2 :
        #             crucible_num = additive_option(count_activity,option[2])
        #         else :
        #             crucible_num = count_activity()
        #         string = string_format('시련의 장',crucible_num)
        #         await message.channel.send(string)
        #     else:
        #         await message.channel.send("어... 수호자님... 뭐라고요...?")
        # #활동
        # elif option[0] == command_list[4]:                
        #     string = random_activity()
        #     string = print_activity(string)
        #     await message.channel.send(string)
        # #레이드
        # elif option[0] == command_list[3]:
        #     string = random_raid()
        #     string = print_raid(string)
        #     await message.channel.send(string)
        
        elif option[0] == '업데이트':
            issue_list = issue_read()
            await message.channel.send("수호자님, 1주일 동안 해결된 문제에 대해서 말씀드릴게요. 음...")
            issue_list = issue_list[:-1]
            date = '1990-11-11'    
            issue_list = sorted(issue_list,key = lambda issue: issue['날짜'])
            for index,issue in enumerate(issue_list):
                title = issue['제목']
                issue_date = issue['날짜']
                if date != issue['날짜']:
                    await message.channel.send(f"{issue_date}, 이 날에는 이런 문제들이 해결되었어요.")
                    date = issue_date
                await message.channel.send(f"{index+1}: {title}")
        else:
            await message.channel.send(error_message)


def additive_option(func_name,option = 'normal'):
    if option == "easy" or option == "라이트":
        result_num = func_name(option = 'easy')
    elif option == "hard" or option == "하드":
        result_num = func_name(option = 'hard')
    else :
        result_num = func_name(option = 'normal')
    return result_num

def count_strike(option='normal'):
    if option == 'easy':
        strike_num = random.randint(1,3)
    else : #normal, hard
        strike_num = random.randint(3,30)
    return strike_num

def count_activity(option='normal'):
    if option == 'easy':
        raid_num = random.randint(1,2)
    elif option == 'hard':
        raid_num = random.randint(5,10)
    else: # option == 'normal':
        raid_num = random.randint(3,6)
    return raid_num


def string_format(option='공격전',num=0):

    string = f"오늘 {option} 몇 판 가야 하나요? {str(num)}판"
    return string

#must be iterator
def multiple_activity(func,num,option = 'normal'):
    activity_dict = dict()
    for _ in range(num):
        find_activity = func(option)
        if find_activity not in activity_dict:
            activity_dict[find_activity] = 1
        else:
            activity_dict[find_activity] += 1
    return activity_dict



client.run(token)