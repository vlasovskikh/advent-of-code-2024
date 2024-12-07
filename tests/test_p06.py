from aoc24 import p06


def test_example_1() -> None:
    lines = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip().splitlines()
    lab = p06.parse_input(lines)
    steps = p06.guard_path(lab)
    assert p06.count_visited_positions(steps) == 41


def test_example_2() -> None:
    lines = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip().splitlines()
    lab = p06.parse_input(lines)
    steps = p06.guard_path(lab)
    assert p06.count_looping_obstacles(lab, steps) == 6


def test_loop1() -> None:
    lines = """
.#..
...#
#^..
....
""".strip().splitlines()
    lab = p06.parse_input(lines)
    steps = p06.guard_path(lab)
    assert p06.count_looping_obstacles(lab, steps) == 1


def test_loop2() -> None:
    lines = """
.#..
...#
.^..
#...
....
""".strip().splitlines()
    lab = p06.parse_input(lines)
    steps = p06.guard_path(lab)
    assert p06.count_looping_obstacles(lab, steps) == 1
