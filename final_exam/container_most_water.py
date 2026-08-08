#!/usr/bin/env python3

import ast

heights = ast.literal_eval(input())

areas = []

left_index = 0

while left_index < len(heights):
    right_index = 0

    while right_index < len(heights):

        if heights[left_index] > heights[right_index]:
            distance = left_index - right_index

            if distance < 0:
                distance *= -1

            areas.append(
                heights[right_index] * distance
            )

        elif heights[right_index] > heights[left_index]:
            distance = left_index - right_index

            if distance < 0:
                distance *= -1

            areas.append(
                heights[left_index] * distance
            )

        else:
            distance = left_index - right_index

            if distance < 0:
                distance *= -1

            areas.append(
                heights[left_index] * distance
            )

        right_index += 1

    left_index += 1

areas.sort()

print(areas[len(areas) - 1])
