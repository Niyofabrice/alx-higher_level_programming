#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n_elements = 0
    for element in range(x):
        try:
            print(my_list[element])
            n_elements += 1
            print()
        except IndexError:
    print()
    return (n_elements)
