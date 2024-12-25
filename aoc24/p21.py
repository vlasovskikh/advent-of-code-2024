from __future__ import annotations
import functools
import typing
from aoc24 import utils


NUM_DATA = [
    list(line)
    for line in [
        "789",
        "456",
        "123",
        ".0A",
    ]
]


DIR_DATA = [
    list(line)
    for line in [
        ".^A",
        "<v>",
    ]
]


class Keypad(typing.NamedTuple):
    next: Keypad | None
    is_num: bool

    @functools.cache
    def keys_len(self, sequence: str) -> int:
        sequence = "A" + sequence
        result = 0
        for c1, c2 in utils.sliding_window(sequence, 2):
            paths = shortest_paths(c1, c2, self.is_num)
            result += min(self.next.keys_len(p) if self.next else len(p) for p in paths)
        return result


def shortest_paths(start: str, end: str, is_num: bool) -> set[str]:
    grid = utils.Grid(NUM_DATA if is_num else DIR_DATA)
    c_start = grid.first(start)
    c_end = grid.first(end)
    d_line, d_col = utils.sub_coord(c_end, c_start)
    path_line = ("v" if d_line > 0 else "^") * abs(d_line)
    path_col = (">" if d_col > 0 else "<") * abs(d_col)
    paths = {
        path_line + path_col,
        path_col + path_line,
    }
    return {p + "A" for p in paths if path_exists(p, grid, c_start)}


def path_exists(path: str, grid: utils.Grid[str], start: utils.Coord) -> bool:
    coord = start
    for c in path:
        match c:
            case "<":
                diff = 0, -1
            case ">":
                diff = 0, 1
            case "^":
                diff = -1, 0
            case "v":
                diff = 1, 0
            case _:
                raise ValueError(f"Unknown symbol {c!r} in path {path!r}")
        coord = utils.add_coord(coord, diff)
        if coord not in grid or grid[coord] == ".":
            return False
    return True


def total_complexity(sequences: list[str], dir_keypads: int) -> int:
    return sum(code_complexity(s, dir_keypads) for s in sequences)


def code_complexity(sequence: str, dir_keypads: int) -> int:
    last = Keypad(next=None, is_num=False)
    keypad = last
    for _ in range(dir_keypads - 1):
        keypad = Keypad(next=keypad, is_num=False)
    first = Keypad(next=keypad, is_num=True)
    shortest = first.keys_len(sequence)
    num = numeric_part(sequence)
    return shortest * num


def numeric_part(sequence: str) -> int:
    return int("".join(n for n in sequence if n.isnumeric()))


def parse_input(lines: list[str]) -> list[str]:
    return lines


def main() -> None:
    sequences = parse_input(utils.read_input_lines(__file__))
    print(total_complexity(sequences, 2))
    print(total_complexity(sequences, 25))


if __name__ == "__main__":
    main()
