def safe_print_list(my_list=[], x=0):
    try:
        n_elements = 0
        for element in range(x):
            print(my_list[element])
            n_elements += 1
        print()
        return n_elements
    except IndexError:
        print()
        return n_elements
