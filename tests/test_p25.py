from aoc24 import p25


def test_example_1() -> None:
    lines = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
""".strip().splitlines()
    locks, keys = p25.parse_input(lines)
    assert p25.count_fitting(locks, keys) == 3
