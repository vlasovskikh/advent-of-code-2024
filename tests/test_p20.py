from aoc24 import p20


def test_example_1() -> None:
    lines = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip().splitlines()
    track = p20.parse_input(lines)
    assert track.count_cheats(2) == {
        2: 14,
        4: 14,
        6: 2,
        8: 4,
        10: 2,
        12: 3,
        20: 1,
        36: 1,
        38: 1,
        40: 1,
        64: 1,
    }


def test_example_2() -> None:
    lines = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip().splitlines()
    track = p20.parse_input(lines)
    cheats = {
        saving: count
        for saving, count in track.count_cheats(20).items()
        if saving >= 50
    }
    assert cheats == {
        50: 32,
        52: 31,
        54: 29,
        56: 39,
        58: 25,
        60: 23,
        62: 20,
        64: 19,
        66: 12,
        68: 14,
        70: 12,
        72: 22,
        74: 4,
        76: 3,
    }
