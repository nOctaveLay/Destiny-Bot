from datetime import date, datetime

__all__ = ['init_raid','init_activity','init_num']

def init_activity():
    today_time = datetime.today().weekday()
    activity_list = ['공격전','황혼전 시련','시련의 장','갬빗','레이드','예언 던전']
    activity_text_dict ={
        activity_list[0]:'수호자, 파란 빡빡이가 선봉대가 해야 하는 **공격전**을 하라고 부르고 있어요.',
        activity_list[1]:'왜 선봉대에 있는 수호자들이 죽어났는지, 알 거 같네요. **황혼전 시련**을 하라고 자발라가 부르고 있어요.',
        activity_list[2]:'샤크스가 요새 바쁜 일이 있냐고 묻네요, **시련의 장**에서 당신의 실력을 보여달래요.',
        activity_list[3]:'방랑자가 당신을 부르고 있어요. 타락한 수호자들을 막아달라네요, **갬빗**에서요.',
        activity_list[4]:'5명의 수호자와 함께, 우리는 **레이드**에서 더 거대한 적을 막아야만 해요.',
        activity_list[5]:'아홉이 당신을 부르고 있어요, **예언**에서요. 빛과 어둠이 무엇일지를 알려준데요.'
    }
    if today_time >4 or today_time < 2:
        activity_list.append('오시리스의 시련')
        activity_text_dict['오시리스의 시련'] = '오, 이런. 오시리스가 등대에 불을 밝혀달라고 그러던데, 생각 있어요?, 당장 **오시리스의 시련**으로 떠나세요.'
    return (activity_list,activity_text_dict)

def init_raid():
    raid_list = ['마지막 소원', '구원의 정원','딥스톤 무덤']
    raid_text_dict = {
        raid_list[0]:'버그가 난무하는 **마지막 소원**도 재미있을것 같아요.',
        raid_list[1]:'선잇기놀이가 재미있는 **구원의 정원**을 추천해요.',
        raid_list[2]:'모든 엑소들의 꿈인 **딥스톤 무덤**은 어떠신가요? 수호자.'
    }
    return (raid_list,raid_text_dict)

def init_num():
    num = 1
    if '번' in option[-1]:
        num_list = option[-1].split("번")
        if num_list[0].isdigit():
            if int(num_list[0]) > 1:
                num = int(num_list[0])
            else: 
                num = -1
    return num
# def random_activity(option = 'normal'):
#     today_time = datetime.today().weekday()    
#     activity_list = ['공격전','황혼전','황혼전 시련','시련의 장','갬빗','레이드']
#     if option == 'hard':
#         hard_activity_list = ['황혼전 시련','갬빗','레이드','이단의 구덩이','조각난 왕관','예언']
#         find_activity = random.choice(hard_activity_list)
#         if find_activity == '황혼전 시련':
#             hard_option = random.choice(['마스터','그랜드마스터'])
#         elif find_activity == '이단의 구덩이' or find_activity == '예언' or find_activity == '조각난 왕관':
#             hard_option = random.choice(['솔로','솔로 무결점','무결점'])
#         elif find_activity == '레이드':
#             hard_option = random.choice(['무결점','업적'])
#         else:
#             hard_option = random.choice(['일반', '프라임'])
#         find_activity += f' {hard_option}'
#         if today_time >4 or today_time < 2:
#             activity_list.append("오시리스의 시련")
#     else:
#         activity_list = ['공격전','황혼전','황혼전 시련','시련의 장','갬빗','레이드']
#         find_activity = random.choice(activity_list)
#     return find_activity
