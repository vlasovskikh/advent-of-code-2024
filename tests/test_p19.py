from aoc24 import p19


def test_example_1() -> None:
    lines = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip().splitlines()
    designs, patterns = p19.parse_input(lines)
    assert p19.count_possible_designs(designs, patterns=patterns) == (6, 16)


def test_small_1() -> None:
    lines = """
bwu, bw, g

bwg
bwr
""".strip().splitlines()
    designs, patterns = p19.parse_input(lines)
    assert p19.count_possible_designs(designs, patterns=patterns) == (1, 1)


def test_small_2() -> None:
    lines = """
bwur, bwu, rb

bwurb
""".strip().splitlines()
    # ...
    designs, patterns = p19.parse_input(lines)
    assert p19.count_possible_designs(designs, patterns=patterns) == (1, 1)


def test_example_1_1() -> None:
    lines = """
r, wr, b, g, bwu, rb, gb, br

rrbgbr
""".strip().splitlines()
    designs, patterns = p19.parse_input(lines)
    assert p19.count_possible_designs(designs, patterns=patterns) == (1, 6)


def test_example_1_2() -> None:
    lines = """
r, wr, b, g, bwu, rb, gb, br

bwurrg
""".strip().splitlines()
    designs, patterns = p19.parse_input(lines)
    assert p19.count_possible_designs(designs, patterns=patterns) == (1, 1)
