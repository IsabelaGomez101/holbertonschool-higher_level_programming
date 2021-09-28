#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    count = 0
    for i in range(0, list_length):
        try:
            tmp = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            tmp = 0
            print("division by 0")
        except TypeError:
            tmp = 0
            print("wrong type")
        except IndexError:
            tmp = 0
            print("out of range")
        finally:
            new_list += [tmp]
    return new_list
