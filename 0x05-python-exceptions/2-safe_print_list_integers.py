#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n_elements = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            n_elements += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (n_elements)
