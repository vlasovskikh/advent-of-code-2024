import collections
import itertools
import typing
from aoc24 import utils


type Gate = tuple[str, str, str, str]


def compile_gates(
    gates: list[Gate],
    swaps: dict[str, str] | None = None,
) -> typing.Callable[[int, int], int]:
    if swaps is None:
        swaps = {}
    swapped: list[Gate] = []
    for in1, op, in2, out1 in gates:
        swapped.append((in1, op, in2, swaps.get(out1, out1)))

    # Assume that xNN and yNN are the initial wires with rank 0
    inputs: set[str] = set()
    for in1, _, in2, _ in gates:
        if in1.startswith(("x", "y")):
            inputs.add(in1)
        if in2.startswith(("x", "y")):
            inputs.add(in2)
    ranks = topological_sort(swapped, inputs)

    def rank(gate: Gate) -> int:
        in1, _, in2, _ = gate
        return max(ranks[in1], ranks[in2])

    ordered = sorted(swapped, key=rank)

    def f(x: int, y: int, bits: int = 45) -> int:
        sources = []

        for i, bit in itertools.zip_longest(range(bits), reversed(to_bits(x))):
            value = int(bit) if bit is not None else 0
            sources.append(f"x{i:02} = {value}")
        for i, bit in itertools.zip_longest(range(bits), reversed(to_bits(y))):
            value = int(bit) if bit is not None else 0
            sources.append(f"y{i:02} = {value}")

        ops = {
            "XOR": "^",
            "OR": "|",
            "AND": "&",
        }

        for in1, op, in2, out1 in ordered:
            sources.append(f"{out1} = {in1} {ops[op]} {in2}")

        vars: dict[str, bool] = {}
        source = "\n".join(sources)
        exec(source, vars)
        return from_bits(vars, "z")

    return f


def calculate_output(gates: list[Gate], input: dict[str, bool]) -> int:
    x = from_bits(input, "x")
    y = from_bits(input, "y")
    f = compile_gates(gates)
    return f(x, y)


def to_bits(x: int) -> list[bool]:
    """Returns the bits of the number, highest bits first."""
    return [bool(int(c)) for c in bin(x)[2:]]


def from_bits(vars: dict[str, bool], name: str) -> int:
    outputs = sorted(
        [(k, v) for k, v in vars.items() if k.startswith(name)],
        reverse=True,
    )
    return int("".join([str(int(v)) for _, v in outputs]), 2)


def topological_sort(gates: list[Gate], inputs: set[str]) -> dict[str, int]:
    results: dict[str, int] = {}
    followers: dict[str, set[str]] = collections.defaultdict(set)
    for in1, _, in2, out1 in gates:
        followers[in1].add(out1)
        followers[in2].add(out1)
    stack: list[tuple[int, str]] = [(0, s) for s in inputs]
    while stack:
        rank, name = stack.pop()
        if name not in results or rank > results[name]:
            results[name] = rank
        for name in followers[name]:
            stack.append(((rank + 1), name))
    return results


def parse_input(lines: list[str]) -> tuple[list[Gate], dict[str, bool]]:
    input_lines, gate_lines = utils.split_by_empty_lines(lines)
    input: dict[str, bool] = {}
    for line in input_lines:
        name, value = line.split(": ")
        input[name] = bool(int(value))
    gates: list[Gate] = []
    for line in gate_lines:
        in1, op, in2, _, out1 = line.split(" ")
        gates.append((in1, op, in2, out1))
    return gates, input


def find_errors(gates: list[Gate]) -> str:
    # Debugged manually after stopping automatically on each AssertionError in this
    # function
    swaps = {
        "z18": "hmt",
        "hmt": "z18",
        "z27": "bfq",
        "bfq": "z27",
        "z31": "hkh",
        "hkh": "z31",
        "fjp": "bng",
        "bng": "fjp",
    }
    f = compile_gates(gates, swaps=swaps)
    combs = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 2),
    ]
    for i in range(45):
        for x, y, expected in combs:
            actual = f(x << i, y << i)
            assert actual == expected << i, (
                f"f({bin(x << i)}, {bin(y << i)}), i: {i}, "
                f"{bin(actual)} != {bin(expected << i)}"
            )
    return ",".join(sorted(swaps.keys()))


def main() -> None:
    gates, input = parse_input(utils.read_input_lines(__file__))
    print(calculate_output(gates, input))
    print(find_errors(gates))


if __name__ == "__main__":
    main()
