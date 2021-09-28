#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    count = 0
    while True:
        try:
            for i in range(count, list_length):
                new_list += [my_list_1[i]/my_list_2[i]]
                count += 1
            return new_list
        except ZeroDivisionError:
            new_list += [0]
            count += 1
            print("division by 0")
        except TypeError:
            new_list += [0]
            count += 1
            print("wrong type")
        except IndexError:
            new_list += [0]
            count += 1
            print("out of range")
