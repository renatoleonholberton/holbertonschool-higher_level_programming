#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = ""
    max_score = 0
    for (key, score) in a_dictionary.items():
        if score > max_score:
            max_score = score
            best_key = key

    return best_key
