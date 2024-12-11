from aoc24 import p11


def test_example_1() -> None:
    lines = """
125 17
""".strip().splitlines()
    stones = p11.parse_input(lines)
    assert p11.count_changed_stones(stones, 25) == 55312


def test_4_steps() -> None:
    lines = """
125 17
""".strip().splitlines()
    stones = p11.parse_input(lines)
    assert p11.count_changed_stones(stones, 4) == 9
