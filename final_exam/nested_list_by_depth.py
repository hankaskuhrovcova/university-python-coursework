#!/usr/bin/env python3

import ast

items = ast.literal_eval(input())


def deep_list(items, depth, result):
    for item in items:
        if isinstance(item, list):
            deep_list(item, depth + 1, result)
        else:
            if depth not in result:
                result[depth] = []
            result[depth].append(item)


result = {}
deep_list(items, 0, result)
print(result)
