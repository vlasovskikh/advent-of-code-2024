from aoc24 import p07


def test_example_1() -> None:
    lines = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip().splitlines()
    equations = p07.parse_input(lines)
    assert p07.total_calibration_result(equations) == 3749


def test_example_2() -> None:
    lines = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip().splitlines()
    equations = p07.parse_input(lines)
    assert p07.total_concat_result(equations) == 11387
