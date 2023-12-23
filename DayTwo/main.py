#!/usr/bin/env python3
# ------------------------------------------------------
# Advent of Code 2023
# Day 2
# Owen Kroeger
# ------------------------------------------------------

import re


def cube_conundrum():
    """Function to read in a line in the form (Game 1: 1 green, 3 blue, 1 red; 2 green 4 blue, 2 red)
    Prints: valid games and sum of their IDs (game is valid if number of cubes pulled on each turn is
    less than the number of those cubes in the bag defined at the top)
    Prints: sum of power of minimum cubes of each color needed in the bag for each game to be possible"""
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14

    red = []
    green = []
    blue = []

    red_items = []
    green_items = []
    blue_items = []

    minimum = 0

    games = []

    pattern = re.compile(r'\d+\s+\w+|\w+\s+\d+')    # parse for game and id group or color and number group
    color_pattern = re.compile(r'(\d+)\s+(\w+)')    # parse only for color and number group (separate groups)

    bad_chars = [':', ';', ',']

    with open("AdventTwo.txt", "r") as f:
        for line in f:

            valid = True

            newline = ''.join(i for i in line if not i in bad_chars)
            matches = re.findall(pattern, newline)

            for item in matches:    # add each color and number group to correct color array
                match = color_pattern.match(item)
                if match:
                    number, color = match.groups()
                    if color == 'red':
                        red.append(item)
                    elif color == 'green':
                        green.append(item)
                    elif color == 'blue':
                        blue.append(item)

            # ----------------------------------
            # Test if games are valid
            for item in red:

                temp = item.split(" ")

                red_items.append(int(temp[0]))

                if int(temp[0]) > red_cubes:
                    valid = False

            for item in green:

                temp = item.split(" ")

                green_items.append(int(temp[0]))

                if int(temp[0]) > green_cubes:
                    valid = False

            for item in blue:

                temp = item.split(" ")

                blue_items.append(int(temp[0]))

                if int(temp[0]) > blue_cubes:
                    valid = False

            if valid:
                temp = matches[0].split(" ")
                games.append(int(temp[-1]))
            # ----------------------------------

            # ----------------------------------
            # Find minimum cubes needed in bag for valid games
            red_max = max(red_items)
            green_max = max(green_items)
            blue_max = max(blue_items)

            minimum += (red_max * green_max * blue_max)
            # ----------------------------------

            red.clear()
            green.clear()
            blue.clear()

            red_items.clear()
            green_items.clear()
            blue_items.clear()

    print(f'Valid Game IDs:', games)
    print(f'Sum of Valid Game IDs:', sum(games))
    print(f'\nSum of powers of minimum req:', minimum)

    f.close()


if __name__ == '__main__':
    cube_conundrum()
