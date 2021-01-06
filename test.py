import random

activity_list = ['공격전','황혼전 시련','시련의 장','갬빗','레이드','예언 던전']
activity_text_dict ={
    activity_list[0]:'수호자, 파란 빡빡이가 선봉대가 해야 하는 **공격전**을 하라고 부르고 있어요.',
    activity_list[1]:'왜 선봉대에 있는 수호자들이 죽어났는지, 알 거 같네요. **황혼전 시련**을 하라고 자발라가 부르고 있어요.',
    activity_list[2]:'샤크스가 요새 바쁜 일이 있냐고 묻네요, **시련의 장**에서 당신의 실력을 보여달래요.',
    activity_list[3]:'방랑자가 당신을 부르고 있어요. 타락한 수호자들을 막아달라네요, **갬빗**에서요.',
    activity_list[4]:'5명의 수호자와 함께, 우리는 **레이드**에서 더 거대한 적을 막아야만 해요.',
    activity_list[5]:'아홉이 당신을 부르고 있어요, **예언**에서요. 빛과 어둠이 무엇일지를 알려준데요.'
}
activity_num_dict = {
    activity_list[0]:3,
    activity_list[1]:2,
    activity_list[2]:0,
    activity_list[3]:5,
    activity_list[4]:4,
    activity_list[5]:0
}

a = {key:0 for key in activity_list}


print(random.choices(activity_list,k=3))