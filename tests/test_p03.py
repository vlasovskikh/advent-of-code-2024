from aoc24 import p03


def test_example_1() -> None:
    lines = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".strip().splitlines()
    s = p03.parse_input(lines)
    assert p03.multiply_not_corrupted_instructions(s, conditionals=False) == 161


def test_example_2() -> None:
    lines = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip().splitlines()
    s = p03.parse_input(lines)
    assert p03.multiply_not_corrupted_instructions(s, conditionals=True) == 48
