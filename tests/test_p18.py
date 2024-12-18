from aoc24 import p18


def test_example_1() -> None:
    lines = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip().splitlines()
    coords = p18.parse_input(lines)
    assert p18.shortest_path(size=(7, 7), coords=coords[:12]) == 22


def test_example_2() -> None:
    lines = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip().splitlines()
    coords = p18.parse_input(lines)
    assert p18.first_blocking_coord(size=(7, 7), coords=coords) == "6,1"
