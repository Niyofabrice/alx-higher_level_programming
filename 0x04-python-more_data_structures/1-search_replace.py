#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for number in range(len(my_list)):
        if my_list[number] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[number])
    return new_list
