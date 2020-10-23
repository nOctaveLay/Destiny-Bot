import discord
import asyncio
import json
import re
import copy
from datetime import date, datetime
import os
import random

client = discord.Client()
token = ${{ secrets.token }}
TIMEVAL = 15
json_route = "./text.json"


@client.event
async def on_ready():
    hello = "안녕하세요."
    print('We have logged in as {0.user}'.format(client))
    # 봇 권한이 있는 곳에만 쓰도록 허락하자.
    for guild in client.guilds:
        for channel in guild.text_channels:            
            print(channel, channel.name == "개발팀")
            if channel.name == "개발팀":
                await channel.send(hello)
                await channel.send("\'#사용법\'을 쳐서 이 아이를 통해 할 수 있는 것을 확인해보세요")


@client.event
async def on_message(message):
    command_list = ['#랜덤 레이드']
    raid_list = ['리바이어던','리바이어던 고급','행성 포식자','행성 포식자 고급','별의 탑','별의 탑 고급','슬픔의 왕관', '마지막 소원', '구원의 정원']
    if message.author.bot:
        return

    if message.content.startswith('#사용법'):
        await message.channel.send("**명령어는 다음과 같아**")
        for content in command_list:
            string = "{}".format(index+1,content)
            await message.channel.send(string)

    if message.content.startswith(command_list[0]):

        def check(m):
            return m.author.bot != True

        find_raid = random.choice(raid_list)
        string = "당신이 가셔야 하는 레이드는 다음과 같습니다 : " +find_raid
        await message.channel.send(string)

client.run(token)
