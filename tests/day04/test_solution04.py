import os
from pathlib import Path
from my_solutions.day04.solution import solve


def test_solution_simple_p1():
    assert solve(read_input("data/simple-input.txt")) == 13


def test_solution_real_p1():
    assert solve(read_input("data/input.txt")) == 25571


def test_solution_simple_p2():
    assert solve(read_input("data/simple-input.txt"), part=2) == 30


def test_solution_real_p2():
    assert solve(read_input("data/input.txt"), part=2) == 8805731


def read_input(file_name) -> list:
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
