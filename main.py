import discord
import asyncio
import json
import re
import copy
from datetime import date, datetime
from configparser import ConfigParser
from issue import issue_read
import os
import random

client = discord.Client()
user = discord.User
config = ConfigParser()
config.read('config.ini')
token = config['default']['token']

TIMEVAL = 15
json_route = "./text.json"

@client.event
async def on_ready():
    hello = "안녕하세요."
    print('We have logged in as {0.user}'.format(client))
    # 봇 권한이 있는 곳에만 쓰도록 허락하자.
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel.name == "개발-테스트":
                await channel.send("으음... 여기가 어디죠?")

@client.event
async def on_message(message):
    call_string = '사기라'
    command_list = ['사용법','랜덤','오늘','레이드','활동','업데이트']
    activity_list = ['공격전','황혼전','황혼전 시련','시련의 장','오시리스의 시련','갬빗','레이드']

    if message.author.bot:
        return

    if message.content.startswith(call_string):
        option = message.content.split(" ")
        option = option[1:]
        if '자발라' in option:
            await message.channel.send("여기서 파란 빡빡이를 왜 찾으시는 거죠?")

        elif len(option) == 0: #사기라만 쳤을 경우
            await message.channel.send("왜 그러시죠? 수호자님?")

        elif option[0] == command_list[0]:
            use_string = usage()
            await message.channel.send(use_string)


        elif option[0] == command_list[1]:
            #랜덤
            if len(option) < 2 or option[1] == command_list[4]:                
                string = random_activity()
                string = print_activity(string)
                await message.channel.send(string)
            #랜덤 레이드
            elif option[1] == command_list[3]:
                string = random_raid()
                string = print_raid(string)
                await message.channel.send(string)
            else:
                string = '수호자님, 그런 명령어는 안 되요.'
                await message.channel.send(string)

        elif option[0] == command_list[2]: #오늘
            if len(option) < 1:
                await message.channel.send("봇을 사용할 수 없습니다, 명령어가 없는게 아닐지?")

            elif len(option) == 1:
                await message.channel.send("오늘 돌아야 하는 것에 대해서 말씀드릴게요.")
                today_count = additive_option(count_activity)
                today_all_dict = multiple_activity(random_activity,today_count)
                for printer_ in print_random_dict(today_all_dict):
                    await message.channel.send(printer_)
            
            elif option[1] == '하드':
                today_count = additive_option(count_activity, option = 'hard')
                today_all_dict = multiple_activity(random_activity,today_count)
                for printer_ in print_random_dict(today_all_dict):
                    await message.channel.send(printer_)

            elif option[1] == '라이트':
                today_count = additive_option(count_activity, option = 'easy')
                today_all_dict = multiple_activity(random_activity,today_count)
                for printer_ in print_random_dict(today_all_dict):
                    await message.channel.send(printer_)

            elif option[1] == "공격전":
                if len(option) == 3:
                    strike_num = additive_option(count_strike,option[2])
                else:
                    strike_num = count_strike()
                string = string_format('공격전',strike_num)
                await message.channel.send(string)

            elif option[1] == "레이드":
                if len(option) == 3:
                    raid_num = additive_option(count_activity,option[2]) 
                else :
                    raid_num = count_activity()
                string = string_format('레이드',raid_num)
                await message.channel.send(string)
                if len(option) > 3 or (len(option) == 3 and (option[2] != '라이트' and option[2] != '하드')):
                    raid_dict = multiple_activity(random_raid,raid_num)
                    for key, value in raid_dict.items():
                        string = print_raid(key)
                        string = string + f" {str(value)}번 정도면 충분할 거 같아요."
                        await message.channel.send(string)

            elif option[1] == "시장" or option[1].startswith("시련"):
                if len(option) >2 :
                    crucible_num = additive_option(count_activity,option[2])
                else :
                    crucible_num = count_activity()
                string = string_format('시련의 장',crucible_num)
                await message.channel.send(string)
            else:
                await message.channel.send("어... 수호자님... 뭐라고요...?")
        #활동
        elif option[0] == command_list[4]:                
            string = random_activity()
            string = print_activity(string)
            await message.channel.send(string)
        #레이드
        elif option[0] == command_list[3]:
            string = random_raid()
            string = print_raid(string)
            await message.channel.send(string)
        
        elif option[0] == command_list[5]:
            issue_list = issue_read()
            await message.channel.send("수호자님, 1주일 동안 해결된 문제에 대해서 말씀드릴게요. 음...")
            issue_list = issue_list[1:]
            date = '1990-11-11'    
            issue_list = sorted(issue_list,key = lambda issue: issue['날짜'])
            for index,issue in enumerate(issue_list):
                title = issue['제목']
                issue_date = issue['날짜']
                if date != issue['날짜']:
                    await message.channel.send(f"{issue_date}, 이 날에는 이런 문제들이 해결되었어요.")
                    date = issue_date
                await message.channel.send(f"{index}, {title}")
        else:
            await message.channel.send("봇을 사용할 수 없습니다, 명령어가 없는게 아닐지?")


def additive_option(func_name,option = 'normal'):
    if option == "라이트":
        result_num = func_name(option = 'easy')
    elif option == "하드":
        result_num = func_name(option = 'hard')
    else :
        result_num = func_name(option = 'normal')
    return result_num

def usage():
    string = '사용법에 대해서 설명하겠습니다.\n'
    with open('use.md','r',encoding = 'utf-8') as f:
        while True:
            temp_string = f.readline()
            if not temp_string :break
            string += temp_string
    return string

def random_raid():
    raid_list = ['리바이어던','행성 포식자','별의 탑','슬픔의 왕관', '마지막 소원', '구원의 정원']
    raid_option = ['일반','고급']
    find_raid = random.choice(raid_list)
    find_raid_option = ''
    if find_raid == raid_list[0] or find_raid == raid_list[1] or find_raid == raid_list[2]:
        find_raid_option = random.choice(raid_option)
    find_raid = find_raid+" "+find_raid_option
    return find_raid

def random_activity():
    today_time = datetime.today().weekday()
    activity_list = ['공격전','황혼전','황혼전 시련','시련의 장','갬빗','레이드']
    if today_time >4 or today_time < 2:
        activity_list.append("오시리스의 시련")
    find_activity = random.choice(activity_list)
    return find_activity

def print_raid(find_raid):
    raid_list = ['리바이어던','행성 포식자','별의 탑','슬픔의 왕관','과거의 고통','마지막 소원', '구원의 정원']
    raid_text_list_single = [
        '레이드를 여러번 하는 느낌을 즐길 수 있는 **리바이어던**이 재미있어요.',
        '레이드 입문으로 괜찮은 **행성포식자**가 좋을 것 같아요.',
        '수호자, 몇 초 지체하면 모두가 폭4하는 **별의 탑**은 어떠신가요?',
        '디버프 폭탄돌리기 메커니즘이 재미있는 **슬픔의 왕관**이 재미있어요',
        '수호자, 가볍게 20분만에 할 수 있는 **과거의 고통**을 해보시는게 어떨까요?',
        '버그가 난무하는 **마지막 소원**도 재미있을것 같아요.',
        '선잇기놀이가 재미있는 **구원의 정원**을 추천해요.'
    ]
    for index,raid in enumerate(raid_list):
        if find_raid.startswith(raid):
            string = raid_text_list_single[index]
            return string

def print_activity(find_):
    today_time = datetime.today().weekday()
    activity_list = ['공격전','황혼전','황혼전 시련','시련의 장','갬빗','레이드']
    if today_time >4 or today_time < 2:
        activity_list.add("오시리스의 시련")
    activity_text_list_single = [
        #fill out this, plz
    ]
    return find_

def print_random_dict(random_dict):
    for key, value in random_dict.items():
        string = f"{key}를 {str(value)}번 정도 돌면 충분할 거 같아요."
        yield string

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
        raid_num = random.randint(1,10)
    else: # option == 'normal':
        raid_num = random.randint(1,5)
    return raid_num


def string_format(option='공격전',num=0):

    string = f"오늘 {option} 몇 판 가야 하나요? {str(num)}판"
    return string

#must be iterator
def multiple_activity(func,num):
    activity_dict = dict()
    for _ in range(num):
        find_activity = func()
        if find_activity not in activity_dict:
            activity_dict[find_activity] = 1
        else:
            activity_dict[find_activity] += 1
    return activity_dict



client.run(token)
