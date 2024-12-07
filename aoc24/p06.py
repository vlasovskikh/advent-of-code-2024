from __future__ import annotations
import enum
import typing
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


class Pos(typing.NamedTuple):
    coord: utils.Coord
    direction: Dir

    def __repr__(self) -> str:
        return f"({self.coord!r}, {self.direction!r})"


class Lab(utils.Grid[Tile]):
    def find_guard(self) -> utils.Coord:
        return next(coord for coord in self if self[coord] == Tile.GUARD)

    def step(
        self,
        pos: Pos,
    ) -> Pos:
        coord, direction = pos
        steps: dict[Dir, utils.Coord] = {
            Dir.UP: utils.Coord(coord.line - 1, coord.pos),
            Dir.RIGHT: utils.Coord(coord.line, coord.pos + 1),
            Dir.DOWN: utils.Coord(coord.line + 1, coord.pos),
            Dir.LEFT: utils.Coord(coord.line, coord.pos - 1),
        }
        new_coord = steps[direction]
        if new_coord in self and self[new_coord] == Tile.OBSTACLE:
            direction = direction.turn90
        else:
            coord = new_coord
        return Pos(coord, direction)

    def path(self, pos: Pos) -> tuple[list[Pos], bool]:
        result: list[Pos] = []
        visited: set[Pos] = set()
        while pos.coord in self and pos not in visited:
            result.append(pos)
            visited.add(pos)
            pos = self.step(pos)
        return result, pos in visited


def guard_path(lab: Lab) -> list[Pos]:
    path, _ = lab.path(Pos(lab.find_guard(), Dir.UP))
    return path


def count_looping_obstacles(
    lab: Lab,
    path: list[Pos],
) -> int:
    obstacles = 0
    visited: set[utils.Coord] = set()
    new_lab = copy.deepcopy(lab)
    for pos in path:
        visited.add(pos.coord)
        new_obstacle = lab.step(pos).coord
        if (
            new_obstacle in lab
            and new_obstacle not in visited
            and lab[new_obstacle] != Tile.OBSTACLE
        ):
            new_lab.data[new_obstacle.line][new_obstacle.pos] = Tile.OBSTACLE
            try:
                _, loop = new_lab.path(pos)
                if loop:
                    obstacles += 1
            finally:
                new_lab.data[new_obstacle.line][new_obstacle.pos] = lab[new_obstacle]
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