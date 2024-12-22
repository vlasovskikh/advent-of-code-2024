from __future__ import annotations
import dataclasses
import enum
import itertools
import os
import typing
from pathlib import Path


def read_input_lines(module_path: str) -> list[str]:
    """Read lines of the input file that corresponds to the module name."""
    with open(input_file_path(module_path), "r") as fd:
        return [s.strip() for s in fd.readlines()]


def input_file_path(module_path: str) -> Path:
    """Input file path from `data/` that corresponds to the module name."""
    p = Path(module_path)  # "<path>/advent-of-code-2023/aoc23/p01.py"
    module_name, _ = os.path.splitext(p.name)
    return p.parent / ".." / "data" / f"{module_name}.txt"


def sliding_window[T](xs: typing.Iterable[T], n: int) -> typing.Iterable[tuple[T, ...]]:
    """Return a sliding window of size `n` for the specified iterable."""
    iterators = itertools.tee(xs, n)
    for shift_count, iterator in enumerate(iterators):
        for _ in range(shift_count):
            next(iterator, None)
    return zip(*iterators)


def split_by_empty_lines(lines: list[str]) -> list[list[str]]:
    """Split a list of lines into sections separated by empty lines in the list."""
    return [list(g) for k, g in itertools.groupby(lines, key=bool) if k]


type Coord = tuple[int, int]


def add_coord(x: Coord, y: Coord) -> Coord:
    return x[0] + y[0], x[1] + y[1]


def sub_coord(x: Coord, y: Coord) -> Coord:
    return x[0] - y[0], x[1] - y[1]


@dataclasses.dataclass
class Grid[T]:
    """2D grid of tiles suitable for maze-like puzzles."""

    data: list[list[T]]
    _size: Coord = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        self._size = len(self.data), len(self.data[0])

    @property
    def size(self) -> Coord:
        return self._size

    def lines(self) -> list[list[Coord]]:
        return [
            [(line, pos) for pos in range(len(self.data[line]))]
            for line in range(len(self.data))
        ]

    def positions(self) -> list[list[Coord]]:
        return [
            [(line, pos) for line in range(len(self.data))]
            for pos in range(len(self.data[0]))
        ]

    def neighbors(self, coord: Coord) -> list[Coord]:
        return self.cross_neighbors(coord) + self.diagonal_neighbors(coord)

    def cross_neighbors(self, coord: Coord) -> list[Coord]:
        results = []
        for line, pos in [
            (coord[0], coord[1] - 1),
            (coord[0], coord[1] + 1),
            (coord[0] - 1, coord[1]),
            (coord[0] + 1, coord[1]),
        ]:
            if 0 <= line < len(self.data) and 0 <= pos < len(self.data[coord[0]]):
                results.append((line, pos))
        return results

    def diagonal_neighbors(self, coord: Coord) -> list[Coord]:
        return [
            (line, pos)
            for line, pos in [
                (coord[0] - 1, coord[1] - 1),
                (coord[0] - 1, coord[1] + 1),
                (coord[0] + 1, coord[1] - 1),
                (coord[0] + 1, coord[1] + 1),
            ]
            if 0 <= line < len(self.data) and 0 <= pos < len(self.data[coord[0]])
        ]

    def __getitem__(self, coord: Coord) -> T:
        return self.data[coord[0]][coord[1]]

    def __setitem__(self, coord: Coord, value: T) -> None:
        self.data[coord[0]][coord[1]] = value

    def __iter__(self) -> typing.Iterator[Coord]:
        for line in range(len(self.data)):
            for pos in range(len(self.data[line])):
                yield line, pos

    def __str__(self) -> str:
        return "\n".join("".join(str(x) for x in line) for line in self.data)

    def __contains__(self, coord: Coord) -> bool:
        lines, positions = self.size
        return 0 <= coord[0] < lines and 0 <= coord[1] < positions


class Dir(enum.IntEnum):
    UP = enum.auto()
    RIGHT = enum.auto()
    DOWN = enum.auto()
    LEFT = enum.auto()

    @property
    def turn90(self) -> Dir:
        match self:
            case Dir.UP:
                return Dir.RIGHT
            case Dir.RIGHT:
                return Dir.DOWN
            case Dir.DOWN:
                return Dir.LEFT
            case Dir.LEFT:
                return Dir.UP

    @property
    def turn270(self) -> Dir:
        match self:
            case Dir.UP:
                return Dir.LEFT
            case Dir.RIGHT:
                return Dir.UP
            case Dir.DOWN:
                return Dir.RIGHT
            case Dir.LEFT:
                return Dir.DOWN

    def __repr__(self):
        match self:
            case Dir.UP:
                return "^"
            case Dir.RIGHT:
                return ">"
            case Dir.DOWN:
                return "v"
            case Dir.LEFT:
                return "<"
