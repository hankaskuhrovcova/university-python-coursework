#!/usr/bin/env python3

import ast

numbers = ast.literal_eval(input())
target = int(input())

seen = set()
pairs = set()

for number in numbers:
    complement = target - number

    if complement in seen:
        pairs.add(
            (complement, number)
        )

    seen.add(number)

print(sorted(pairs))
