#!/usr/bin/env python3

import ast

data = ast.literal_eval(input())
target_key = input()


def find_key(data, target_key):
    for key, value in data.items():

        if key == target_key:
            return value

        if isinstance(value, dict):
            result = find_key(value, target_key)

            if result is not None:
                return result

    return None


print(find_key(data, target_key))
