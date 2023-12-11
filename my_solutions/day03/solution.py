def solve(data: str, part: int = 1) -> int:
    matrix = build_matrix(data)
    if part == 1:
        return sum(get_part_numbers(matrix))
    if part == 2:
        return sum(get_grear_ratios(matrix))


def get_grear_ratios(matrix: list) -> list:
    ratios = []
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if not is_symbol(char):
                continue
            adjacents = check_matrix(matrix, x, y, is_number)
            if len(adjacents) != 2:
                continue
            ratio = 1
            for adjacent in adjacents:
                ratio *= get_gear_ratio(matrix, adjacent[0], adjacent[1])
            ratios.append(ratio)
    return ratios


def get_gear_ratio(matrix: list, x: int, y: int) -> list:
    # now we get the grear ratio
    # this is a number of chars around the the coords
    number = matrix[y][x]
    # get all chars to the right
    for i in range(x + 1, len(matrix[0])):
        if matrix[y][i].isdigit():
            number += matrix[y][i]
        else:
            break
    # get all chars to the left
    for i in range(x - 1, -1, -1):
        if matrix[y][i].isdigit():
            number = matrix[y][i] + number
        else:
            break
    return int(number)


def get_part_numbers(matrix: list) -> list:
    numbers = []
    x = 0
    y = 0
    while y < len(matrix):
        while x < len(matrix[0]):
            if matrix[y][x].isdigit():
                # read ahead until we find a symbol
                start_x = x
                while x < len(matrix[0]) and matrix[y][x].isdigit():
                    x += 1
                number = int("".join(matrix[y][start_x:x]))
                # check if there is a symbol adjacent to all the digits
                for i in range(start_x, x):
                    if len(check_matrix(matrix, i, y)) > 0:
                        numbers.append(number)
                        break
            else:
                x += 1
        y += 1
        x = 0
    return numbers


def build_matrix(data: str) -> list:
    matrix = []
    for line in data:
        matrix.append([*line])
    return matrix


def is_symbol(symbol: str) -> bool:
    # check if symbol is a symbol
    # a symbol is a character that is not a dot or a number
    return symbol not in [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def is_number(symbol: str) -> bool:
    # check if symbol is a number
    return symbol.isdigit()


def check_matrix(
    matrix: list, x: int, y: int, check_char: callable = is_symbol
) -> list[tuple]:
    # check if there is a symbal adjacent to x,y
    # if there is, return True
    adjacents = []
    # symbol to the right?
    if x + 1 < len(matrix[0]) and check_char(matrix[y][x + 1]):
        adjacents.append((x + 1, y))
    # symbol to the left?
    if x - 1 >= 0 and check_char(matrix[y][x - 1]):
        adjacents.append((x - 1, y))
    # symbol to the top?
    if y - 1 >= 0 and check_char(matrix[y - 1][x]):
        adjacents.append((x, y - 1))
    # symbol to the bottom?
    if y + 1 < len(matrix) and check_char(matrix[y + 1][x]):
        adjacents.append((x, y + 1))
    # symbol to the top right?
    if (
        x + 1 < len(matrix[0])
        and y - 1 >= 0
        and check_char(matrix[y - 1][x + 1])
        and not check_char(matrix[y - 1][x])
    ):
        adjacents.append((x + 1, y - 1))
    # symbol to the top left?
    if (
        x - 1 >= 0
        and y - 1 >= 0
        and check_char(matrix[y - 1][x - 1])
        and not check_char(matrix[y - 1][x])
    ):
        adjacents.append((x - 1, y - 1))
    # symbol to the bottom right?
    if (
        x + 1 < len(matrix[0])
        and y + 1 < len(matrix)
        and check_char(matrix[y + 1][x + 1])
        and not check_char(matrix[y + 1][x])
    ):
        adjacents.append((x + 1, y + 1))
    # symbol to the bottom left?
    if (
        x - 1 >= 0
        and y + 1 < len(matrix)
        and check_char(matrix[y + 1][x - 1])
        and not check_char(matrix[y + 1][x])
    ):
        adjacents.append((x - 1, y + 1))
    return adjacents
