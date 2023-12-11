import os
from pathlib import Path
from my_solutions.day01.solution import solve


def test_solution_simple_p1():
    assert solve(read_input("data/simple-input.txt")) == 142


def test_solution_real_p1():
    assert solve(read_input("data/input.txt")) == 55090


def test_solution_simple_p2():
    assert solve(read_input("data/simple-input-p2.txt"), part=2) == 281


def test_solution_real_p2():
    assert solve(read_input("data/input.txt"), part=2) == 54845


def read_input(file_name) -> list:
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
