def solve(data: str, part: int = 1) -> int:
    if part == 1:
        return sum([calc_points(*a) for a in get_numbers(data)])
    else:
        return solve2(data)


def solve2(data: str) -> int:
    pile = [1 for _ in range(len(data))]
    for i, (winning_numbers, actual_numbers) in enumerate(get_numbers(data)):
        equals = number_of_equals(winning_numbers, actual_numbers)
        for j in range(i + 1, i + equals + 1):
            pile[j] += pile[i]
    return sum(pile)


def get_numbers(data: str) -> list[tuple[list[int], list[int]]]:
    for line in data:
        winning_numbers, actual_numbers = [
            list(map(int, list(filter(None, a.split(" ")))))
            for a in line.split(":")[1].split("|")
        ]
        yield winning_numbers, actual_numbers


def calc_points(winning_numbers: list[int], actual_numbers: list[int]) -> int:
    points = number_of_equals(winning_numbers, actual_numbers)
    return 2 ** (points - 1) if points > 0 else 0


def number_of_equals(winning_numbers: list[int], actual_numbers: list[int]) -> int:
    return sum([1 for a in actual_numbers if a in winning_numbers])
