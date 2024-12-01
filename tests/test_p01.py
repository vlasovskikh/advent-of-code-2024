from aoc24 import p01


def test_example_1() -> None:
    lines = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip().splitlines()
    xs, ys = p01.parse_input(lines)
    assert p01.total_distance(xs, ys) == 11


def test_example_2() -> None:
    lines = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip().splitlines()
    xs, ys = p01.parse_input(lines)
    assert p01.similarity_score(xs, ys) == 31
