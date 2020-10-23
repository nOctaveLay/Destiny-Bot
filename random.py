import discord
import asyncio
import json
import re
import copy
from datetime import date, datetime
import os
import random

client = discord.Client()
token = $$(secret_key)
TIMEVAL = 15
json_route = "./text.json"


def save_json(event_list):
    with open("./text.json", 'w', encoding='utf-8-sig') as make_file:
        json.dump(event_list, make_file, indent='\t', ensure_ascii=False)


def load_json():
    if os.path.getsize(json_route) < 6:
        event_list = dict()
    else:
        with open("./text.json", 'r', encoding='utf-8-sig') as f:
            event_list = json.load(f)
    return event_list


@client.event
async def on_ready():
    hello = "안녕하세요."
    print('We have logged in as {0.user}'.format(client))
    # 봇 권한이 있는 곳에만 쓰도록 허락하자.
    for guild in client.guilds:
        if guild.name == '개인채널':
            for channel in guild.text_channels:
                await channel.send(hello)


@client.event
async def on_message(message):
    command_list = ['#랜덤 레이드']
    raid_list = ['리바이어던','리바이어던 고급','행성 포식자','별의 탑','슬픔의 왕관', '마지막 소원', '구원의 정원']
    if message.author.bot:
        return

    if message.content.startswith('#help'):
        await message.channel.send("**명령어는 다음과 같아**")
        for x in command_list:
            await message.channel.send("* " + x)

    if message.content.startswith(command_list[0]):

        def check(m):
            return m.author.bot != True

        while True:
            try:
                find_raid = random.choice(command_list)
                await message.channel.send("당신이 가셔야 하는 레이드는 다음과 같습니다 : %s" %find_raid)
