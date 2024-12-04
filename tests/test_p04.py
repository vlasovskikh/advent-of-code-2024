from aoc24 import p04


def test_example_1() -> None:
    lines = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip().splitlines()
    grid = p04.parse_input(lines)
    assert p04.count_xmas(grid) == 18


def test_example_2() -> None:
    lines = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip().splitlines()
    grid = p04.parse_input(lines)
    assert p04.count_x_mas(grid) == 9
