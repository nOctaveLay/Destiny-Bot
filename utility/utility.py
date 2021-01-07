import random

__all__ = ['usage','choosen','print_dict','print_no_named']

def choosen(choose_list,option = 'normal'):
    choosen_value = random.choice(choose_list)
    return choosen_value

def print_dict(choosen_string,choosen_dict):
    string = choosen_dict[choosen_string]
    return string

def print_no_named():
    result_string = f"수호자님, 음... 이 보스는 역할 분배를 하지 않아도 되는 보스인 거 같아요."
    return result_string

def repeat_func(function,num):
    for _ in range(num):
        function()

def usage(file_name = './use.md'):
    string = '사용법에 대해서 설명하겠습니다.\n'
    with open(file_name,'r',encoding = 'utf-8') as f:
        while True:
            temp_string = f.readline()
            if not temp_string :break
            string += temp_string
    return string
