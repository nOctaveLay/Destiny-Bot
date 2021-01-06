import random

__all__ = ['print_lw_named','print_lw_no_named','print_lw_sec_named','print_lw_third_named','print_lw_forth_named']

def print_lw_sec_named():
    result_string = "[2네임드] "
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    result_string += f"1번:{people_list[0]}, 2번:{people_list[1]}, 3번:{people_list[2]}, 4번:{people_list[3]} \n[서포터] {people_list[4]}, {people_list[5]}"
    return result_string

def print_lw_third_named():
    result_string = "[3네임드] "
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    result_string += f"[왼쪽] 둘 다 - {people_list[0]}, 1번째 정화 - {people_list[1]}, 2번째 정화 - {people_list[2]} \n[오른쪽] 첫번째+마지막 - {people_list[4]}, 하나씩 - {people_list[5]}, {people_list[6]}"
    return result_string

def print_lw_forth_named():
    result_string = "[4네임드] "
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    result_string += f"[계단] 발판-{people_list[0]} 러너-{people_list[1]}\n[돌] 발판-{people_list[2]} 러너-{people_list[3]}\n[나무] 발판-{people_list[4]} 러너-{people_list[5]}"
    return result_string

def print_lw_no_named(num:int):
    result_string = f"[{str(num)}네임드] - 역할 분배가 존재하지 않음"
    return result_string

def print_lw_named():
    result_string = print_lw_no_named(1) + "\n"
    result_string += print_lw_sec_named() + "\n"
    result_string += print_lw_third_named() + "\n"
    result_string += print_lw_forth_named()
    return result_string

