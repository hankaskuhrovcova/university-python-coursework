#!/usr/bin/env python3

text = input()
substrings = []

index = 1
count = 0

while index < len(text):
    if text[index] == text[index - 1]:
        count += 1
    index += 1

if count == len(text):
    print(text[0])
else:
    index = 1
    remaining_text = ""

    while index < len(text):
        if text[index - 1] == text[index]:
            inner_index = index

            while inner_index < len(text):
                remaining_text += text[inner_index]
                inner_index += 1
        else:
            break

        index += 1

    if len(remaining_text) > 0:
        text = remaining_text

    index = 0
    current_substring = ""

    while index < len(text):
        if text[index] not in current_substring:
            current_substring += text[index]
            index += 1
        else:
            break

    if index == len(text):
        substrings.append(text)

    if len(substrings) < 1:
        index = 0
        current_substring = ""

        while index < len(text):
            if text[index] not in current_substring:
                current_substring += text[index]
                index += 1
            else:
                substrings.append(current_substring)
                current_substring = ""

    longest = substrings[0]
    index = 0

    while index < len(substrings):
        if len(substrings[index]) > len(longest):
            longest = substrings[index]
        index += 1

    print(longest)
