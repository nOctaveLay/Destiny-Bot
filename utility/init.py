from datetime import date, datetime

__all__ = ['change_activity_text_dict','change_raid_text_dict','init_activity','init_num']

def change_activity_text_dict(act_num_dict):
    activity_list = ['공격전','황혼전 시련','시련의 장','갬빗','레이드','예언','선각자']
    new_text_dict = list()
    today_time = datetime.today().weekday()
    for x in act_num_dict:
        num = act_num_dict[x]
        num_text = f'**{num}번** ' if num > 0 else ''  
        if num > 0:
            if x == activity_list[0]:
                new_text_dict.append(f'수호자, 파란 빡빡이가 선봉대가 해야 하는 **공격전**을 {num_text}하라고 부르고 있어요.')
            elif x == activity_list[1]:
                new_text_dict.append(f'왜 선봉대에 있는 수호자들이 죽어났는지, 알 거 같네요. **황혼전 시련**을 {num_text}하라고 자발라가 부르고 있어요.')
            elif x == activity_list[2]:
                new_text_dict.append(f'샤크스가 요새 바쁜 일이 있냐고 묻네요, **시련의 장**에서 당신의 실력을 {num_text}보여달래요.')
            elif x == activity_list[3]:
                new_text_dict.append(f'방랑자가 당신을 부르고 있어요. 타락한 수호자들을 막아달라네요, **갬빗**에서요. {num_text}정도면 충분하데요. 이유를 모르겠다니까요.')
            elif x == activity_list[4]:
                new_text_dict.append(f'5명의 수호자와 함께, 우리는 **레이드**에서 더 거대한 적을 막아야만 해요. {num_text}정도면 충분하다고 선봉대장이 말하네요.')
            elif x == activity_list[5]:
                new_text_dict.append(f'아홉이 당신을 {num_text}부르고 있어요, **예언**에서요. 빛과 어둠이 무엇일지를 알려준데요.')
            elif x == activity_list[6]:
                new_text_dict.append(f'매 한마리가 당신을 보며 {num_text}울부짖고 있어요. **선각자**를 찾고 있나봐요.')
            elif (today_time >4 or today_time < 2) and x == '오시리스의 시련':
                new_text_dict.append(f'오, 이런. 오시리스가 등대에 불을 밝혀달라고 그러던데, 생각 있어요?, 당장 **오시리스의 시련**으로 {num_text}떠나세요.')
            else:
                print(x)
                pass
    return new_text_dict

def change_raid_text_dict(raid_num_dict):
    raid_list = ['마지막 소원', '구원의 정원','딥스톤 무덤']
    new_text_dict = list()
    for x in raid_num_dict:
        num = raid_num_dict[x]
        num_text = f'**{num}번** ' if num > 1 else ''  
        if num > 0:
            if x == raid_list[0]:
                new_text_dict.append(f'마라 소프 여왕이 부르고 있어요, **마지막 소원**을 빌었던 곳에서 리븐을 {num_text}죽여달래요. 재밌을 거 같지 않나요?')
            elif x == raid_list[1]:
                new_text_dict.append(f'선잇기놀이가 재미있는 **구원의 정원**이면 {num_text}도는 것도 나쁘지 않을까요?')
            elif x == raid_list[2]:
                new_text_dict.append(f'모든 엑소들의 꿈인 **딥스톤 무덤**을 {num_text}도는 것은 어떠신가요? 수호자.')
            else:
                print(x)
                pass
    return new_text_dict

def init_activity():
    today_time = datetime.today().weekday()
    activity_list = ['공격전','황혼전 시련','시련의 장','갬빗','레이드','예언','선각자']
    if today_time >4 or today_time < 2:
        activity_list.append('오시리스의 시련')
    return activity_list

def init_num(option):
    num = 1
    if '번' in option or '회' in option:
        temp_num = option[:-1]
    else:
        temp_num = option
    if temp_num.isdigit():
        if int(temp_num) > 1:
            num = int(temp_num)
        else: 
            num = -1
    return num
