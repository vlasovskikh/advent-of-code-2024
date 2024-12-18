from aoc24 import p17


def test_example_1() -> None:
    lines = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip().splitlines()
    program, state = p17.parse_input(lines)
    assert p17.interpret_program(program, state) == "4,6,3,5,6,3,5,2,1,0"
