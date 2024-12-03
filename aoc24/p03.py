import re
from typing import Sequence

from aoc24 import utils


def parse_input(lines: Sequence[str]) -> str:
    return "\n".join(lines)


def multiply_not_corrupted_instructions(s: str, *, conditionals: bool) -> int:
    res = 0
    enabled = True
    for m in re.finditer(r"(mul)\(([0-9]{1,3}),([0-9]{1,3})\)|(do)\(\)|(don't)\(\)", s):
        if enabled and m.group(1) == "mul":
            x = int(m.group(2))
            y = int(m.group(3))
            res += x * y
        elif conditionals and m.group(4) == "do":
            enabled = True
        elif conditionals and m.group(5) == "don't":
            enabled = False
    return res


def main() -> None:
    s = parse_input(utils.read_input_lines(__file__))
    print(multiply_not_corrupted_instructions(s, conditionals=False))
    print(multiply_not_corrupted_instructions(s, conditionals=True))


if __name__ == "__main__":
    main()
