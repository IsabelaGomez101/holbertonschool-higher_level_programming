#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary.values()) == 0:
        return None
    nmax = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == nmax:
            return key
