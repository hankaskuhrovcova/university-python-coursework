#!/usr/bin/env python3

first_text = input()
second_text = input()

first_set = set(first_text)
second_set = set(second_text)

intersection = first_set & second_set
union = first_set | second_set

result = (
    len(intersection)
    / len(union)
)

print(result)
