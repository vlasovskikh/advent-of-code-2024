from aoc24 import p14


def test_example_1() -> None:
    lines = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip().splitlines()
    robots = p14.parse_input(lines)
    assert p14.safety_factor(robots, size=(11, 7), seconds=100) == 12
