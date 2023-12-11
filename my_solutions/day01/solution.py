numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solve(data: str, part: int = 1):
    numbers = []
    for line in data:
        number = ""
        for i, _ in enumerate(line):
            is_digit, digit = check_number(line, i, part)
            if is_digit:
                number += digit
                break

        for i, _ in enumerate(line):
            is_digit, digit = check_number(line, len(line) - i - 1, part)
            if is_digit:
                number += digit
                break
        numbers.append(int(number))
    return sum(numbers)


def check_number(word: str, index: int, part: int = 1):
    if part == 2 and not word[index].isdigit():
        short_word = word[index:]
        for number in numbers:
            if short_word.startswith(number):
                return (True, str(numbers[number]))

    return (word[index].isdigit(), word[index])
