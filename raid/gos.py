import random

__all__ = ['print_gos_named','print_gos_first_named','print_gos_sec_named','print_gos_third_named','print_gos_forth_named']

def print_gos_first_named():
    result_string = "**1네임드**\n"
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    boss_list = sorted(people_list[0:3])
    connect_list = sorted(people_list[3:6])
    result_string += f"**보스**({boss_list[0]}, {boss_list[1]}, {boss_list[2]}), **연결**({connect_list[0]}, {connect_list[1]}, {connect_list[2]})"
    return result_string

def print_gos_sec_named():
    result_string = "**2네임드**\n"
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    result_string += f"**6시**({people_list[0]}), **9시**({people_list[1]})\n**12시**({people_list[2]}), **3시**({people_list[3]})\n**12-3시**({people_list[4]}), **6-9시**({people_list[5]})"
    return result_string

def print_gos_third_named():
    result_string = "**3네임드**\n"
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    boss_list = sorted(people_list[0:3])
    connect_list = sorted(people_list[3:6])
    result_string += f"**보스**({boss_list[0]}, {boss_list[1]}, {boss_list[2]})\n**티끌**({connect_list[0]}, {connect_list[1]}, {connect_list[2]})"
    return result_string

def print_gos_forth_named():
    result_string = "**4네임드**\n"
    people_list = [x+1 for x in range(6)]
    random.shuffle(people_list)
    mote1_list = sorted(people_list[0:2])
    mote2_list = sorted(people_list[2:4])
    floor_list = sorted(people_list[4:6])
    result_string += f"**티끌1**({mote1_list[0]}, {mote1_list[1]})\n**티끌2**({mote2_list[0]}, {mote2_list[1]})\n**발판**({floor_list[0]}, {floor_list[1]})"
    return result_string

def print_gos_named():
    result_string = print_gos_first_named() + "\n\n"
    result_string += print_gos_sec_named() + "\n\n"
    result_string += print_gos_third_named() + "\n\n"
    result_string += print_gos_forth_named()
    return result_string

