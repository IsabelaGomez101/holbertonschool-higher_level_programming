#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = dict(sorted(a_dictionary.items()))
    for i in new_dic:
        print("{:s}: {}".format(i, new_dic[i]))
