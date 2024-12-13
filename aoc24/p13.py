import dataclasses
import re
from aoc24 import utils


@dataclasses.dataclass
class Machine:
    a: utils.Coord
    b: utils.Coord
    prize: utils.Coord

    def min_tokens(self) -> int:
        x_a, y_a = self.a
        x_b, y_b = self.b
        x_p, y_p = self.prize
        x1 = round(x_a * (y_p * x_b - x_p * y_b) / (y_a * x_b - y_b * x_a))
        x2 = x_p - x1
        presses: list[utils.Coord] = [
            (x1 // x_a, (x_p - x1) // x_b),
            (x2 // x_a, (x_p - x2) // x_b),
        ]
        result = [3 * a + b for a, b in presses if self.press((a, b)) == self.prize]
        if len(result) == 0:
            return 0
        elif len(result) == 1:
            return result[0]
        else:
            return min(result)

    def press(self, count: utils.Coord) -> utils.Coord:
        a, b = count
        return (
            self.a[0] * a + self.b[0] * b,
            self.a[1] * a + self.b[1] * b,
        )


def min_tokens(machines: list[Machine]) -> int:
    return sum(machine.min_tokens() for machine in machines)


def min_tokens_fixed(machines: list[Machine]) -> int:
    fix = 10_000_000_000_000
    fixed = [
        Machine(a=m.a, b=m.b, prize=(m.prize[0] + fix, m.prize[1] + fix))
        for m in machines
    ]
    return min_tokens(fixed)


def parse_input(lines: list[str]) -> list[Machine]:
    result: list[Machine] = []
    for line_a, line_b, line_prize in utils.split_by_empty_lines(lines):
        m = re.match(r"Button A: X\+([0-9]+), Y\+([0-9]+)", line_a)
        if not m:
            raise ValueError(f"Unknown line: {line_a!r}")
        a = int(m.group(1)), int(m.group(2))
        m = re.match(r"Button B: X\+([0-9]+), Y\+([0-9]+)", line_b)
        if not m:
            raise ValueError(f"Unknown line: {line_b!r}")
        b = int(m.group(1)), int(m.group(2))
        m = re.match(r"Prize: X=([0-9]+), Y=([0-9]+)", line_prize)
        if not m:
            raise ValueError(f"Unknown line: {line_prize!r}")
        prize = int(m.group(1)), int(m.group(2))
        result.append(Machine(a=a, b=b, prize=prize))
    return result


def main() -> None:
    parsed = parse_input(utils.read_input_lines(__file__))
    print(min_tokens(parsed))
    print(min_tokens_fixed(parsed))


if __name__ == "__main__":
    main()
