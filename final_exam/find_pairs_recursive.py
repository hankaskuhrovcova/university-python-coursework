#!/usr/bin/env python3

import ast

numbers = ast.literal_eval(input())
target = int(input())


def find_pairs(numbers, target, result):
    if len(numbers) == 0 or len(numbers) == 1:
        return result
    else:
        for number in numbers[1:]:
            if (target - numbers[0]) == number:
                if (numbers[0], number) not in result:
                    result.append((numbers[0], number))

        return find_pairs(numbers[1:], target, result)


print(find_pairs(numbers, target, []))
