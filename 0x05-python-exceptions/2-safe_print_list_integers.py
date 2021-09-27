#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
        aux = len_print = 0
        while True:
            try:
                if aux < x:
                    print("{:d}".format(my_list[aux]), end="")
                    len_print += 1
                    aux += 1
                else:
                    print("")
                    return len_print
            except (ValueError, TypeError):
                pass
                aux += 1
