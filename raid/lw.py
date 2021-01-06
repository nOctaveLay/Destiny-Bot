import random

__all__ = ['print_lw_named','print_lw_no_named','print_lw_sec_named','print_lw_third_named','print_lw_forth_named']

def print_lw_sec_named():
    result_string = "**2네임드**\n"
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    supporter_list = sorted(people_list[4:6])
    result_string += f"**1번**({people_list[0]}), **2번**({people_list[1]})\n**3번**({people_list[2]}), **4번**({people_list[3]})\n**서포터**({supporter_list[0]}, {supporter_list[1]})"
    return result_string

def print_lw_third_named():
    result_string = "**3네임드**\n"
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    supporter_list = sorted(people_list[4:6])
    result_string += f"**왼쪽**- 둘 다({people_list[0]}), 정화1({people_list[1]}), 정화2({people_list[2]}) \n**오른쪽**- 첫번째+마지막({people_list[3]}), 하나씩({supporter_list[0]}, {supporter_list[1]})"
    return result_string

def print_lw_forth_named():
    result_string = "**4네임드**\n"
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    result_string += f"**계단** 발판({people_list[0]}), 러너({people_list[1]})\n**돌** 발판({people_list[2]}) 러너({people_list[3]})\n**나무** 발판({people_list[4]}), 러너({people_list[5]})"
    return result_string

def print_lw_no_named():
    result_string = f"수호자님, 음... 이 보스는 역할 분배를 하지 않아도 되는 보스인 거 같아요."
    return result_string

def print_lw_named():
    result_string = print_lw_sec_named() + "\n\n"
    result_string += print_lw_third_named() + "\n\n"
    result_string += print_lw_forth_named()
    return result_string

