#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0
    for number in range(len(my_list)):
        if my_list[number] in new_list:
            continue
        else:
            result += my_list[number]
            new_list.append(my_list[number])
    return result
