#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = "Last digit of"
n = number % 10
if number < 0:
    n = (abs(number) % 10) * -1
if n > 5:
    print("{} {} is {} and is greater than 5".format(ld, number, n))
elif n == 0:
    print("{} {} is {} and is 0".format(ld, number, n))
else:
    print("{} {} is {} and is less than 6 and not 0".format(ld, number, n))
