from __future__ import annotations
import collections
import dataclasses
import functools
import heapq
import itertools
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


@dataclasses.dataclass
class Keypad:
    nested: Keypad | None
    is_num: bool

    def how_to_type(self, sequence: str) -> set[str]:
        result: set[str] = set()
        if self.nested:
            sequences = ["A" + s for s in self.nested.how_to_type(sequence)]
        else:
            sequences = [sequence]
        for sequence in sequences:
            segments: list[set[str]] = []
            for c1, c2 in utils.sliding_window(sequence, 2):
                segments.append(shortest_paths(c1, c2, self.is_num))
            for comb in itertools.product(*segments):
                result.add("".join(comb))
        if len(result) == 0:
            return result
        min_len = min(len(s) for s in result)
        return {s for s in result if len(s) == min_len}


@functools.cache
def shortest_paths(start: str, end: str, is_num: bool) -> set[str]:
    grid = utils.Grid(NUM_DATA if is_num else DIR_DATA)
    c_start = grid.first(start)
    c_end = grid.first(end)
    traceback = shortest_paths_traceback(grid, c_start)
    paths = all_paths(c_start, c_end, traceback)
    return {path_to_keys(path) for path in paths}


def path_to_keys(path: list[utils.Coord]) -> str:
    keys: list[str] = []
    for c1, c2 in utils.sliding_window(path, 2):
        diff = utils.sub_coord(c2, c1)
        match diff:
            case (0, 1):
                key = ">"
            case (0, -1):
                key = "<"
            case (1, 0):
                key = "v"
            case (-1, 0):
                key = "^"
            case _:
                raise ValueError(f"Unsupported diff: {diff}")
        keys.append(key)
    keys.append("A")
    return "".join(keys)


def all_paths(
    c_start: utils.Coord,
    c_end: utils.Coord,
    traceback: dict[utils.Coord, set[utils.Coord]],
) -> list[list[utils.Coord]]:

    paths: list[list[utils.Coord]] = []
    stack: list[tuple[utils.Coord, list[utils.Coord]]] = [(c_end, [])]
    while stack:
        coord, path = stack.pop()
        path.append(coord)
        if coord == c_start:
            paths.append(list(reversed(path)))
        for prev in traceback[coord]:
            path = path.copy()
            stack.append((prev, path))

    return paths


def shortest_paths_traceback(
    grid: utils.Grid[str],
    c_start: utils.Coord,
) -> dict[utils.Coord, set[utils.Coord]]:
    best_score: dict[utils.Coord, int] = {}
    traceback: dict[utils.Coord, set[utils.Coord]] = collections.defaultdict(set)
    heap: list[tuple[int, utils.Coord, utils.Coord]] = [(0, c_start, c_start)]

    while heap:
        score, coord, prev = heapq.heappop(heap)
        if coord in best_score and score > best_score[coord]:
            continue
        best_score[coord] = score
        if prev != coord:
            traceback[coord].add(prev)
        for n in grid.cross_neighbors(coord):
            if grid[n] != ".":
                heapq.heappush(heap, (score + 1, n, coord))

    return traceback


def total_complexity(sequences: list[str], prefix: str = "A") -> int:
    return sum(code_complexity(prefix + s) for s in sequences)


def code_complexity(sequence: str) -> int:
    radiation = Keypad(nested=None, is_num=True)
    frozen = Keypad(nested=radiation, is_num=False)
    historic = Keypad(nested=frozen, is_num=False)
    shortest = min(len(keys) for keys in historic.how_to_type(sequence))
    num = numeric_part(sequence)
    return shortest * num


def numeric_part(sequence: str) -> int:
    return int("".join(n for n in sequence if n.isnumeric()))


def parse_input(lines: list[str]) -> list[str]:
    return lines


def main() -> None:
    # 196582: too high
    # 188398
    sequences = parse_input(utils.read_input_lines(__file__))
    print(total_complexity(sequences))


if __name__ == "__main__":
    main()
