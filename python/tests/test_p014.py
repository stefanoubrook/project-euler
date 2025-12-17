from solutions.p014 import get_collatz_length, solve


def test_solve_example():
    assert get_collatz_length(13) == 10


def test_small_range():
    assert solve(4) == 3
