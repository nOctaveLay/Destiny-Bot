import discord
import asyncio
import json
import re
import copy
from datetime import date, datetime
from configparser import ConfigParser
import os
import random

client = discord.Client()
token = #hidden
TIMEVAL = 15
json_route = "./text.json"

@client.event
async def on_ready():
    hello = "안녕하세요."
    print('We have logged in as {0.user}'.format(client))
    # 봇 권한이 있는 곳에만 쓰도록 허락하자.
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel.name == "개발팀":
                await channel.send(hello)
                await channel.send("\'#사용법\'을 쳐서 이 아이를 통해 할 수 있는 것을 확인해보세요")


@client.event
async def on_message(message):
    command_list = ['#사용법','#랜덤','#오늘']

    if message.author.bot:
        return

    if message.content.startswith('#사용법'):
        use_string = usage()
        await message.channel.send(use_string)
    if message.content.startswith('#'):
        if message.content.startswith(command_list[1]):
            option = message.content.split(" ")

            def check(m):
                return m.author.bot != True
            if option[1] == "레이드":
                string = random_raid()
                await message.channel.send(string)
        elif message.content.startswith(command_list[2]):
            option = message.content.split(" ")
            if option[1] == "공격전":
                if (len(option) == 3) and option[2] == "라이트":
                    string = count_strike(option = 'light')
                else:
                    string = count_strike()
                await message.channel.send(string)
        else:
            await message.channel.send("봇을 사용할 수 없습니다, 명령어가 없는게 아닐지?")



def usage():
    string = '사용법에 대해서 설명하겠습니다.\n'
    with open('README.md','r',encoding = 'utf-8') as f:
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
    if find_raid == find_raid[0] or find_raid == find_raid[1] or find_raid == find_raid[2]:
        find_raid_option = random.choice(raid_option)
    string = "당신이 가셔야 하는 레이드는 다음과 같습니다 : " + find_raid + " " + find_raid_option
    return string

def count_strike(option = 'normal'):
    if option == 'normal':
        strike_num = random.randint(3,50)
    else :
        strike_num = random.randint(1,10)
    strike_num = str(strike_num)
    string = "오늘 공격전 몇 판 가야 하나요? {}판".format(strike_num)
    return string
client.run(token)
