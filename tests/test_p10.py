from aoc24 import p10


def test_example_1() -> None:
    lines = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip().splitlines()
    grid = p10.parse_input(lines)
    assert grid.sum_trailhead_scores(by_rating=False) == 36


def test_example_2() -> None:
    lines = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip().splitlines()
    grid = p10.parse_input(lines)
    assert grid.sum_trailhead_scores(by_rating=True) == 81
