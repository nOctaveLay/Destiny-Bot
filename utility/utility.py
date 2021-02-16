import random

__all__ = ['usage','choosen','print_dict']

def choosen(choose_list,option = 'normal'):
    choosen_value = random.choice(choose_list)
    return choosen_value

def print_dict(choosen_string,choosen_dict):
    string = choosen_dict[choosen_string]
    return string

def usage(file_name = './data/use.md'):
    string = '사용법에 대해서 설명하겠습니다.\n'
    with open(file_name,'r',encoding = 'utf-8') as f:
        while True:
            temp_string = f.readline()
            if not temp_string :break
            string += temp_string
    return string
