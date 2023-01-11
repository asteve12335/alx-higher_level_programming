#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    max_student = list(a_dictionary)[0]
    max_score = a_dictionary[max_student]
    for k, v in a_dictionary.items():
        if v > max_score:
            max_score = v
            max_student = k
    return max_student
