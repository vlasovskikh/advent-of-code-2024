from aoc24 import p12


def test_example_1_1() -> None:
    lines = """
AAAA
BBCD
BBCC
EEEC
""".strip().splitlines()
    garden = p12.parse_input(lines)
    assert garden.total_fencing_price() == 140


def test_example_2_1() -> None:
    lines = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""".strip().splitlines()
    garden = p12.parse_input(lines)
    assert garden.total_fencing_price() == 772


def test_example_3_1() -> None:
    lines = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip().splitlines()
    garden = p12.parse_input(lines)
    assert garden.total_fencing_price() == 1930


def test_example_1_2() -> None:
    lines = """
AAAA
BBCD
BBCC
EEEC
""".strip().splitlines()
    garden = p12.parse_input(lines)
    assert garden.total_price_with_discount() == 80


def test_example_2_2() -> None:
    lines = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""".strip().splitlines()
    garden = p12.parse_input(lines)
    assert garden.total_price_with_discount() == 436


def test_example_4() -> None:
    lines = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
""".strip().splitlines()
    garden = p12.parse_input(lines)
    assert garden.total_price_with_discount() == 236


def test_example_5() -> None:
    lines = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
""".strip().splitlines()
    garden = p12.parse_input(lines)
    assert garden.total_price_with_discount() == 368


def test_example_3_2() -> None:
    lines = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip().splitlines()
    garden = p12.parse_input(lines)
    assert garden.total_price_with_discount() == 1206
