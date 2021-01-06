import random

__all__ = ['print_dsc_named','print_dsc_first_named','print_dsc_sec_named','print_dsc_forth_named']

def print_dsc_first_named():
    result_string = "**1네임드**\n"
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    black_list = sorted(people_list[2:4])
    white_list = sorted(people_list[4:6])
    result_string += f"**조작**({people_list[0]}), **스캐너**({people_list[1]})\n**검은방**({black_list[0]}, {black_list[1]})\n**흰 방**({white_list[0]}, {white_list[1]})"
    return result_string

def print_dsc_sec_named():
    result_string = "**2네임드**\n"
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    first_list = sorted(people_list[4:6])
    result_string += f"**조작**({people_list[0]}), **스캐너2**({people_list[1]}), **2층**({people_list[2]})\n**스캐너1**({people_list[3]}, **1층**({first_list[0]}, {first_list[1]}))"
    return result_string

def print_dsc_forth_named():
    result_string = "**4네임드**\n"
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    mote1_list = sorted(people_list[0:2])
    mote2_list = sorted(people_list[2:4])
    floor_list = sorted(people_list[4:6])
    result_string += f"**조작**({mote1_list[0]}, {mote1_list[1]})\n**스캐너**({mote2_list[0]}, {mote2_list[1]})\n**억압**({floor_list[0]}, {floor_list[1]})"
    return result_string

def print_dsc_named():
    result_string = print_dsc_first_named() + "\n\n"
    result_string += print_dsc_sec_named() + "\n\n"
    result_string += print_dsc_forth_named()
    return result_string

