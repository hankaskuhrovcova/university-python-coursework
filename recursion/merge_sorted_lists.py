#!/usr/bin/env python3

import ast

list_a = ast.literal_eval(input())
list_b = ast.literal_eval(input())


def merge(list_a, list_b):
    if len(list_a) == 0:
        return list_b

    elif len(list_b) == 0:
        return list_a

    elif list_a[0] < list_b[0]:
        return [list_a[0]] + merge(
            list_a[1:], list_b
        )

    else:
        return [list_b[0]] + merge(
            list_a, list_b[1:]
        )


print(merge(list_a, list_b))
