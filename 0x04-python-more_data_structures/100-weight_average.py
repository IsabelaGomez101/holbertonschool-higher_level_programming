#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    prom = 0
    for i in my_list:
        average += i[0] * i[1]
        prom += i[1]
    return average/prom
