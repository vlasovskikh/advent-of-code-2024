from aoc24 import p21


def test_example_1() -> None:
    lines = """
029A
980A
179A
456A
379A
""".strip().splitlines()
    sequences = p21.parse_input(lines)
    assert p21.total_complexity(sequences, 2) == 126384


def test_small_1() -> None:
    lines = """
029A
""".strip().splitlines()
    sequences = p21.parse_input(lines)
    assert p21.total_complexity(sequences, 2) == 68 * 29


def test_small_5() -> None:
    lines = """
379A
""".strip().splitlines()
    sequences = p21.parse_input(lines)
    assert p21.total_complexity(sequences, 2) == 64 * 379
