#!/usr/bin/env python3

text = input()


def skip(text, step):
    if text == "":
        return ""
    else:
        return text[0] + skip(text[step + 1:], step + 1)


print(skip(text, 0))
