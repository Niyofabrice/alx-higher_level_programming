#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for number in range(len(my_list)):
        if my_list[number] == search:
            my_list[number] = replace
    return my_list
