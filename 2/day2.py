import re
from functools import reduce

with open("input.txt", "r") as f:
    data = f.read().splitlines()
    f.close()


colors = {"blue": 14, "red": 12, "green": 13}


def partOne():
    total = 0
    for game, index in data:
        is_game_possible = True
        for color, max_of_color in colors.items():
            is_game_possible = not any(
                [int(n) > max_of_color for n in re.findall(f"\d+(?= {color})", game)]
            )
            if not is_game_possible:
                break

        if is_game_possible:
            total += index

    print(total)


def partTwo():
    print(
        sum(
            [
                reduce(
                    lambda x, y: x * y,
                    [
                        max([int(n) for n in re.findall(f"\d+(?= {color})", game)])
                        for color in colors
                    ],
                )
                for game in data
            ]
        )
    )


partOne()
partTwo()
