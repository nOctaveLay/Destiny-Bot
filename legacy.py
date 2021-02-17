        # elif option[0] == '오늘': #오늘
        #     if len(option) < 1:
        #         await message.channel.send("봇을 사용할 수 없습니다, 명령어가 없는게 아닐지?")

        #     elif len(option) == 1:
        #         await message.channel.send("오늘 돌아야 하는 것에 대해서 말씀드릴게요.")
        #         today_count = additive_option(count_activity)
        #         today_all_dict = multiple_activity(random_activity,today_count)
        #         for printer_ in print_random_dict(today_all_dict):
        #             await message.channel.send(printer_)

        #     elif option[1] == '하드':
        #         mode = random.randint(0,1)
        #         if mode == 0:
        #             option_set = ['easy','hard']
        #         else:
        #             option_set = ['hard','easy']
        #         today_count = additive_option(count_activity, option = option_set[0])
        #         today_all_dict = multiple_activity(random_activity,today_count,option = option_set[1])
        #         for printer_ in print_random_dict(today_all_dict):
        #             await message.channel.send(printer_)
        #     elif option[1] == '라이트':
        #         today_count = additive_option(count_activity, option = 'easy')
        #         today_all_dict = multiple_activity(random_activity,today_count)
        #         for printer_ in print_random_dict(today_all_dict):
        #             await message.channel.send(printer_)

        #     elif option[1] == "공격전":
        #         if len(option) == 3:
        #             strike_num = additive_option(count_strike,option[2])
        #         else:
        #             strike_num = count_strike()
        #         string = string_format('공격전',strike_num)
        #         await message.channel.send(string)

        #     elif option[1] == "레이드":
        #         if len(option) == 3:
        #             raid_num = additive_option(count_activity,option[2])
        #         else :
        #             raid_num = count_activity()
        #         string = string_format('레이드',raid_num)
        #         await message.channel.send(string)
        #         if len(option) > 3 or (len(option) == 3 and (option[2] != '라이트' and option[2] != '하드')):
        #             raid_dict = multiple_activity(random_raid,raid_num)
        #             for key, value in raid_dict.items():
        #                 string = print_raid(key)
        #                 string = string + f" {str(value)}번 정도면 충분할 거 같아요."
        #                 await message.channel.send(string)

        #     elif option[1] == "시장" or option[1].startswith("시련"):
        #         if len(option) >2 :
        #             crucible_num = additive_option(count_activity,option[2])
        #         else :
        #             crucible_num = count_activity()
        #         string = string_format('시련의 장',crucible_num)
        #         await message.channel.send(string)
        #     else:
        #         await message.channel.send("어... 수호자님... 뭐라고요...?")
        # #활동
        # elif option[0] == command_list[4]:
        #     string = random_activity()
        #     string = print_activity(string)
        #     await message.channel.send(string)
        # #레이드
        # elif option[0] == command_list[3]:
        #     string = random_raid()
        #     string = print_raid(string)
        #     await message.channel.send(string)



# def repeat_func(function,num):
#     for _ in range(num):
#         function()
