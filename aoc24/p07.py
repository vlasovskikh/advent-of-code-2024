import itertools
import math
import operator
import typing


from aoc24 import utils


class Equation(typing.NamedTuple):
    result: int
    numbers: list[int]


def concat(x: int, y: int) -> int:
    return x * (10 ** math.ceil(math.log10(y + 1))) + y


def is_solvable(
    equation: Equation,
    possible_ops: list[typing.Callable[[int, int], int]],
) -> bool:
    ops_count = len(equation.numbers) - 1
    for ops in itertools.product(possible_ops, repeat=ops_count):  # 2 ** n
        s, *rest = equation.numbers
        for op, n in zip(ops, rest):
            s = op(s, n)
        if s == equation.result:
            return True
    return False


def total_calibration_result(equations: list[Equation]) -> int:
    possible_ops = [operator.mul, operator.add]
    return sum(e.result for e in equations if is_solvable(e, possible_ops))


def total_concat_result(equations: list[Equation]) -> int:
    possible_ops = [operator.mul, operator.add, concat]
    return sum(e.result for e in equations if is_solvable(e, possible_ops))


def parse_input(lines: list[str]) -> list[Equation]:
    split_lines = [line.split(":") for line in lines]
    return [
        Equation(int(result), [int(n) for n in numbers.strip().split()])
        for result, numbers in split_lines
    ]


def main() -> None:
    equations = parse_input(utils.read_input_lines(__file__))
    print(total_calibration_result(equations))
    print(total_concat_result(equations))


if __name__ == "__main__":
    main()
