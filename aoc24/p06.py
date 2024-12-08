from __future__ import annotations
import enum
import copy

from aoc24 import utils


class Tile(enum.StrEnum):
    EMPTY = "."
    OBSTACLE = "#"
    GUARD = "^"
    NEW_OBSTACLE = "O"


class Dir(enum.Enum):
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


type Pos = tuple[utils.Coord, Dir]


class Lab(utils.Grid[Tile]):
    def find_guard(self) -> utils.Coord:
        return next(coord for coord in self if self[coord] == Tile.GUARD)

    def step(self, pos: Pos) -> Pos:
        c, d = pos
        match d:
            case Dir.UP:
                return self.step_in_dir(c, d, (c[0] - 1, c[1]))
            case Dir.RIGHT:
                return self.step_in_dir(c, d, (c[0], c[1] + 1))
            case Dir.DOWN:
                return self.step_in_dir(c, d, (c[0] + 1, c[1]))
            case Dir.LEFT:
                return self.step_in_dir(c, d, (c[0], c[1] - 1))
            case _:
                raise ValueError(f"Unknown direction: {d}")

    def step_in_dir(
        self, coord: utils.Coord, direction: Dir, new_coord: utils.Coord
    ) -> Pos:
        if new_coord in self and self[new_coord] == Tile.OBSTACLE:
            direction = direction.turn90
        else:
            coord = new_coord
        return coord, direction

    def path(self, pos: Pos) -> tuple[list[Pos], bool]:
        result: list[Pos] = []
        visited: set[Pos] = set()
        while pos[0] in self and pos not in visited:
            result.append(pos)
            visited.add(pos)
            pos = self.step(pos)
        return result, pos in visited


def guard_path(lab: Lab) -> list[Pos]:
    path, _ = lab.path((lab.find_guard(), Dir.UP))
    return path


def count_looping_obstacles(
    lab: Lab,
    path: list[Pos],
) -> int:
    obstacles = 0
    visited: set[utils.Coord] = set()
    new_lab = copy.deepcopy(lab)
    for pos in path:
        visited.add(pos[0])
        new_obstacle = lab.step(pos)[0]
        if (
            new_obstacle in lab
            and new_obstacle not in visited
            and lab[new_obstacle] != Tile.OBSTACLE
        ):
            new_lab[new_obstacle] = Tile.OBSTACLE
            try:
                _, loop = new_lab.path(pos)
                if loop:
                    obstacles += 1
            finally:
                new_lab[new_obstacle] = lab[new_obstacle]
    return obstacles


def parse_input(lines: list[str]) -> Lab:
    return Lab([[Tile(c) for c in line] for line in lines])


def count_visited_positions(path: list[Pos]) -> int:
    return len({coord for coord, _ in path})


def main() -> None:
    lab = parse_input(utils.read_input_lines(__file__))
    path = guard_path(lab)
    print(count_visited_positions(path))
    print(count_looping_obstacles(lab, path))


if __name__ == "__main__":
    main()
