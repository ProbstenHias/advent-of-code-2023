from math import prod

total_cubes = {"red": 12, "green": 13, "blue": 14}


def solve(data: str, part: int = 1):
    if part == 1:
        return solve_part1(data)
    return solve_part2(data)


def solve_part2(data: str):
    total = 0
    for line in data:
        fewest_cubes = parse_line2(line)
        total += prod(fewest_cubes.values())
    return total


def solve_part1(data: str):
    total = 0
    for i, line in enumerate(data):
        if parse_line(line):
            total += i + 1
    return total


def parse_line(line: str) -> bool:
    line = line.replace(":", ";")
    draws = line.split(";")[1:]
    for draw in draws:
        colors = draw.split(",")
        for color in colors:
            if color.endswith("red"):
                red = int(color.split(" ")[1])
                if red > total_cubes["red"]:
                    return False
            elif color.endswith("green"):
                green = int(color.split(" ")[1])
                if green > total_cubes["green"]:
                    return False
            elif color.endswith("blue"):
                blue = int(color.split(" ")[1])
                if blue > total_cubes["blue"]:
                    return False
    return True


def parse_line2(line: str) -> dict:
    line = line.replace(":", ";")
    draws = line.split(";")[1:]
    max_red = 0
    max_green = 0
    max_blue = 0
    for draw in draws:
        colors = draw.split(",")
        for color in colors:
            if color.endswith("red"):
                red = int(color.split(" ")[1])
                max_red = max(red, max_red)
            elif color.endswith("green"):
                green = int(color.split(" ")[1])
                max_green = max(green, max_green)
            elif color.endswith("blue"):
                blue = int(color.split(" ")[1])
                max_blue = max(blue, max_blue)
    return {"red": max_red, "green": max_green, "blue": max_blue}
