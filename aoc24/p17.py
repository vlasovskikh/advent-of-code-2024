import dataclasses
import enum
import re
import typing

from aoc24 import utils


INSTRUCTION_SIZE = 2


class OpCode(enum.IntEnum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


@dataclasses.dataclass
class Instruction:
    opcode: OpCode
    operand: int


@dataclasses.dataclass
class State:
    a: int
    b: int
    c: int
    ip: int = 0


def interpret_program(program: list[Instruction], state: State) -> str:
    result: list[int] = []
    while state.ip < len(program) * INSTRUCTION_SIZE:
        instruction = program[state.ip // INSTRUCTION_SIZE]
        output = interpret_instruction(instruction, state)
        if output is not None:
            result.append(output)
    return ",".join(str(x) for x in result)


def interpret_instruction(instruction: Instruction, state: State) -> int | None:
    match instruction.opcode:
        case OpCode.ADV:
            adv(instruction.operand, state)
        case OpCode.BXL:
            bxl(instruction.operand, state)
        case OpCode.BST:
            bst(instruction.operand, state)
        case OpCode.JNZ:
            jnz(instruction.operand, state)
        case OpCode.BXC:
            bxc(state)
        case OpCode.OUT:
            return out(instruction.operand, state)
        case OpCode.BDV:
            bdv(instruction.operand, state)
        case OpCode.CDV:
            cdv(instruction.operand, state)
        case _:
            raise ValueError(f"Unknown instruction: {instruction}")
    return None


def adv(operand: int, state: State) -> None:
    state.a = state.a // (2 ** combo(operand, state))
    state.ip += INSTRUCTION_SIZE


def bxl(operand: int, state: State) -> None:
    state.b = state.b ^ operand
    state.ip += INSTRUCTION_SIZE


def bst(operand: int, state: State) -> None:
    state.b = combo(operand, state) % 8
    state.ip += INSTRUCTION_SIZE


def jnz(operand: int, state: State) -> None:
    if state.a != 0:
        state.ip = operand
    else:
        state.ip += INSTRUCTION_SIZE


def bxc(state: State) -> None:
    state.b = state.b ^ state.c
    state.ip += INSTRUCTION_SIZE


def out(operand: int, state: State) -> int | None:
    result = combo(operand, state) % 8
    state.ip += INSTRUCTION_SIZE
    return result


def bdv(operand: int, state: State) -> None:
    state.b = state.a // (2 ** combo(operand, state))
    state.ip += INSTRUCTION_SIZE


def cdv(operand: int, state: State) -> None:
    state.c = state.a // (2 ** combo(operand, state))
    state.ip += INSTRUCTION_SIZE


def combo(operand: int, state: State) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return state.a
        case 5:
            return state.b
        case 6:
            return state.c
        case _:
            raise ValueError(f"Unknown combo operand: {operand}")


def parse_input(lines: list[str]) -> tuple[list[Instruction], State]:
    registers, program = utils.split_by_empty_lines(lines)
    state = State(0, 0, 0)
    for register in registers:
        m = re.match(r"Register ([A-Z]): ([0-9]+)", register)
        if not m:
            raise ValueError(f"Unknown register line: {register!r}")
        name = m.group(1)
        value = int(m.group(2))
        setattr(state, name.lower(), value)
    assert len(program) == 1
    m = re.match("Program: ([0-9,]+)", program[0])
    if not m:
        raise ValueError(f"Unknown program line: {program}")
    numbers = [int(s) for s in m.group(1).split(",")]
    instructions = [
        Instruction(OpCode(opcode), operand)
        for opcode, operand in (zip(numbers[::2], numbers[1::2]))
    ]
    return instructions, state


def f_iter(a: int, b: int, c: int) -> typing.Iterator[int]:
    """Disassembled puzzle input from data/p17.txt."""
    while True:
        b = (a % 8) ^ 3  # Lowest 3 bits of `a`. b = 0..7
        c = a // (2**b)  # 2**b = 1..128. c = 1/128..1 * a. c = a >> 0..7
        b = (b ^ c) ^ 3  # Change last 3 then 2 bits of c. b = c-7..c+7
        a = a // 8  # a = a >> 3
        yield b % 8  # Lowest 3 bits of `b`
        if a == 0:
            return


def f(a: int) -> list[int]:
    return list(f_iter(a, 0, 0))


def heuristic_input_search_for_our_program() -> int:
    """
    f(a=?) = [2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0]

    The value of `a` must be in range (8 ** 15, 8 ** 16 - 1) = (2 ** 45, 2 ** 48 - 1) =
    (35184372088832, 281474976710655), because we yield one value for each 3 bits of
    `a`.

    I calculated it in REPL using a technique similar to this one:

    >>> y = [2, 4, 1, 3, 7, 5, 4, 0, 1, 3, 0, 3, 5, 5, 3, 0]
    >>> c = 33
    >>> p = 0b011_000_001_100_101_111_001_100_111_111_101
    >>> {bin((i << c) + p)[2:][:-c]: p17.f((i << c) + p)
    ... for i in range(1 << 15)
    ... if p17.f(((i << c) + p))[:16] == y}
    {'11000100101001': [2, 4, 1, 3, 7, 5, 4, 0, 1, 3, 0, 3, 5, 5, 3, 0]}
    """
    return int("11000100101001_011_000_001_100_101_111_001_100_111_111_101", base=2)


def main() -> None:
    program, state = parse_input(utils.read_input_lines(__file__))
    print(interpret_program(program, state))
    print(heuristic_input_search_for_our_program())


if __name__ == "__main__":
    main()
