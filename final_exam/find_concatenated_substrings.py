#!/usr/bin/env python3

import ast

word_list = ast.literal_eval(input())
text = input()

if len(word_list) != 0:
    word_count = len(word_list)
    word_length = len(word_list[0])

    sections = []
    index = 0

    while index < len(text) - (word_count * word_length):
        sections.append(
            text[index:index + word_length * word_count]
        )
        index += 1

    sections.append(
        text[len(text) - word_length * word_count:]
    )

    result = []

    for position, section in enumerate(sections):
        used_words = []
        index = 0

        while index < len(section):
            if (
                section[index:index + word_length] in word_list
                and section[index:index + word_length] not in used_words
            ):
                used_words.append(
                    section[index:index + word_length]
                )

            index += word_length

        if len(used_words) == word_count:
            result.append(position - 1)

    print(result)

else:
    print(word_list)
