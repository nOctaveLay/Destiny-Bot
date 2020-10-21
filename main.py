import discord
import asyncio
import json
import re
import copy
from datetime import date, datetime
import os

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
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        if guild.name == '개인채널':
            for channel in guild.text_channels:
                await channel.send("UMP45가 왔습니다. 지휘관, 사이좋게 지내자♩♪")
                await channel.send("궁금한 명령어가 있다면 #help로 봐줘 ♩♪")
    event_list = load_json()
    today = date.today()
    del_event_list = []
    temp_event_list = event_list.copy()
    for x in event_list:
        e_mon = event_list[x]['end']['mon']
        e_day = event_list[x]['end']['day']
        end_day = date(today.year, int(e_mon), int(e_day))
        if (end_day - today).days < 0:
            del_event_list.append(temp_event_list[x])
            del temp_event_list[x]
    save_json(temp_event_list)
    client.loop.create_task(time_track())


@client.event
async def on_message(message):
    command_list = ['#set', '#show']
    if message.author.bot:
        return

    if message.content.startswith('#help'):
        await message.channel.send("**명령어는 다음과 같아**")
        for x in command_list:
            await message.channel.send("* " + x)

    if message.content.startswith(command_list[0]):

        def check(m):
            return m.author.bot != True

        event = dict()

        while True:
            try:
                await message.channel.send("이벤트 뭐하더라?")
                await message.channel.send("국지전 -> 국지전. 1지~6지 보스 처치는 보스. 인형 파밍은 파밍이라고 알려줘.")
                type_ = await client.wait_for('message', timeout=60, check=check)
                if type_.content is None: raise TimeoutError
                if type_.content.startswith("국지전"):
                    type_ = "국지전";break
                elif type_.content.startswith("보스"):
                    type_ = "보스";break
                elif type_.content.startswith("파밍"):
                    type_ = "파밍";break
                else:
                    raise TimeoutError
            except asyncio.TimeoutError:
                await message.channel.send("이런 일, 별로 없었는데 말이…지…. 다시 시도해줘.")

        while True:
            try:
                await message.channel.send('시작 날짜가 언제더라? 지휘관♩♪')
                start_date = await client.wait_for('message', timeout=60, check=check)
                if start_date.content is not None:
                    break
            except asyncio.TimeoutError:
                await message.channel.send("이런 일, 별로 없었는데 말이…지…. 다시 시도해줘.")

        while True:
            try:
                await message.channel.send('시작 날짜가 언제더라? 지휘관♩♪')
                start_date = await client.wait_for('message', timeout=60, check=check)
                if start_date.content is not None:
                    break
            except asyncio.TimeoutError:
                await message.channel.send("이런 일, 별로 없었는데 말이…지…. 다시 시도해줘.")

        while True:
            try:
                await message.channel.send('종료 날짜가 언제더라? 지휘관♩♪')
                end_date = await client.wait_for('message', timeout=60, check=check)
                if end_date.content is not None:
                    break
            except asyncio.TimeoutError:
                await message.channel.send("이런 일, 별로 없었는데 말이…지…. 다시 시도해줘.")
                return

        start_date = start_date.content.replace(" ", "")
        start_date = re.findall(r"[\d]+", start_date)
        end_date = end_date.content.replace(" ", "")
        end_date = re.findall(r"[\d]+", end_date)
        msg = ''
        event_list = load_json()
        event = dict()
        s, d = dict(), dict()
        if len(start_date) == 3:
            msg += start_date[0] + "년 "
            s["year"] = start_date[0]
        s["mon"], s["day"] = start_date[-2], start_date[-1]
        msg += start_date[-2] + "월 " + start_date[-1] + "일부터 "
        if len(end_date) == 3:
            msg += end_date[0] + "년 "
            d["year"] = end_date[0]
        msg += end_date[-2] + "월 " + end_date[-1] + "일까지라는 거지?♪"
        await message.channel.send(msg)
        d["mon"], d["day"] = end_date[-2], end_date[-1]
        event["start"] = s
        event["end"] = d
        event_list[type_] = event
        save_json(event_list)
        await message.channel.send("ok, 처리 완료야 지휘관.♪")

    if message.content.startswith(command_list[1]):  # show
        if os.path.getsize(json_route) < 6:
            await message.channel.send("지금 이벤트는 없어. 쉬기 딱 좋은 날씨네♬")
        else:
            event_list = load_json()
            await message.channel.send("지금 있는 이벤트는 이거야, 지휘관.")
            for x in event_list:
                elem_start, elem_end = event_list[x]['start'], event_list[x]['end']
                s_mon, s_day = elem_start['mon'], elem_start['day']
                e_mon, e_day = elem_end['mon'], elem_start['day']
                await message.channel.send(x)
                await message.channel.send(s_mon + "월 " + s_day + "일부터")
                await message.channel.send(e_mon + "월 " + e_day + "일까지")
                await message.channel.send("----------------------------")


@client.event
async def time_track():
    a = 0
    while True:
        today = datetime.now()
        await asyncio.sleep(1)
        msg = []
        if today.hour == 22 and a == 0:
            msg.append("이벤트를 잘 잊어버리는 지휘관을 위한 알람이야 ♪♬")
            event_list = load_json()
            event_type = list(event_list.keys())
            if "국지전" in event_type:
                msg.append("국지전, 새벽 4시까지 2번 하는 거 잊지마♪♬")
                msg.append("찍신이 지휘관과 함께하기를? 랄까♪♬")
            if "보스" in event_type:
                msg.append("1지 - 6지 보스를 한 번씩 죽이는 거 잊지마♪♬")
            if "파밍" in event_type:
                msg.append("파밍 꼭 했길 바래 ♬")
            for guild in client.guilds:
                for channel in guild.text_channels:
                    for x in msg:
                        await channel.send(x)
                    a += 1

        if today.hour == 13 and a == 0:
            for guild in client.guilds:
                for channel in guild.text_channels:
                    for x in msg:
                        await channel.send("전지, 캐야되는거. 잊지마 지휘관")
                    a += 1


client.run(token)
