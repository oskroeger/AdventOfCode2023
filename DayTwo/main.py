import re


def cube_conundrum():

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

    pattern = re.compile(r'\d+\s+\w+|\w+\s+\d+')
    color_pattern = re.compile(r'(\d+)\s+(\w+)')

    bad_chars = [':', ';', ',']

    with open("AdventTwo.txt", "r") as f:
        for line in f:

            valid = True

            newline = ''.join(i for i in line if not i in bad_chars)
            matches = re.findall(pattern, newline)

            for item in matches:
                match = color_pattern.match(item)
                if match:
                    number, color = match.groups()
                    if color == 'red':
                        red.append(item)
                    elif color == 'green':
                        green.append(item)
                    elif color == 'blue':
                        blue.append(item)

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

            red_max = max(red_items)
            green_max = max(green_items)
            blue_max = max(blue_items)

            minimum += (red_max * green_max * blue_max)

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
