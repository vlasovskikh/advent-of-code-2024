from aoc24 import p02


def test_example_1() -> None:
    lines = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip().splitlines()
    assert p02.safe_reports_count(p02.parse_input(lines)) == 2


def test_example_2() -> None:
    lines = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip().splitlines()
    assert p02.tolerant_safe_reports_count(p02.parse_input(lines)) == 4
