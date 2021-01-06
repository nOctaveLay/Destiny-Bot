import random

__all__ = ['print_lw_named','print_lw_first_named','print_lw_sec_named','print_lw_third_named','print_lw_forth_named']

def print_lw_first_named():
    result_string = "[1네임드] "
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    boss_list = sorted(people_list[0:3])
    connect_list = sorted(people_list[3:6])
    result_string += f"보스- {boss_list[0]}, {boss_list[1]}, {boss_list[2]} 연결- {connect_list[0]}, {connect_list[1]}, {connect_list[2]}"
    return result_string

def print_lw_sec_named():
    result_string = "[2네임드] "
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    result_string += f"6시:{people_list[0]}, 9시:{people_list[1]}, 12시:{people_list[2]}, 3시:{people_list[3]} \n[서포터] 12-3시:{people_list[4]}, 6-9시:{people_list[5]}"
    return result_string

def print_lw_third_named():
    result_string = "[3네임드] "
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    boss_list = sorted(people_list[0:3])
    connect_list = sorted(people_list[3:6])
    result_string += f"보스- {boss_list[0]}, {boss_list[1]}, {boss_list[2]} 티끌- {connect_list[0]}, {connect_list[1]}, {connect_list[2]}"
    return result_string

def print_lw_forth_named():
    result_string = "[4네임드] "
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    result_string += f"티끌 1조- {people_list[0]}, {people_list[1]} 티끌 2조- {people_list[2]}, {people_list[3]} 발판조- {people_list[4]}, {people_list[5]}"
    return result_string

def print_lw_named():
    result_string = print_lw_first_named() + "\n"
    result_string += print_lw_sec_named() + "\n"
    result_string += print_lw_third_named() + "\n"
    result_string += print_lw_forth_named()
    return result_string

