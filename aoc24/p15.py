from __future__ import annotations
import dataclasses
import enum

from aoc24 import utils


class Cell(enum.StrEnum):
    SPACE = "."
    BOX = "O"
    WALL = "#"
    ROBOT = "@"
    LEFT_BOX = "["
    RIGHT_BOX = "]"


class Move(enum.StrEnum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"


class Warehouse(utils.Grid[Cell]):
    robot: utils.Coord = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        super().__post_init__()
        self.robot = next(c for c in self if self[c] == Cell.ROBOT)

    def widen(self) -> Warehouse:
        new_data: list[list[Cell]] = []
        for line in self.data:
            new_line: list[Cell] = []
            for cell in line:
                new_line.extend(self.widen_cell(cell))
            new_data.append(new_line)
        return Warehouse(new_data)

    def widen_cell(self, cell: Cell) -> list[Cell]:
        match cell:
            case Cell.SPACE:
                return [Cell.SPACE, Cell.SPACE]
            case Cell.BOX:
                return [Cell.LEFT_BOX, Cell.RIGHT_BOX]
            case Cell.WALL:
                return [Cell.WALL, Cell.WALL]
            case Cell.ROBOT:
                return [Cell.ROBOT, Cell.SPACE]
            case _:
                raise ValueError(f"Cannot widen cell type {cell}")

    def sum_boxes_coordinates_after_moves(self, moves: list[Move]) -> int:
        self.run_moves(moves)
        return self.sum_boxes_coordinates()

    def sum_boxes_coordinates(self) -> int:
        return sum(
            [
                c[0] * 100 + c[1]
                for c in self
                if self[c] == Cell.BOX or self[c] == Cell.LEFT_BOX
            ]
        )

    def run_moves(self, moves: list[Move]) -> None:
        for move in moves:
            self.run_move(move)

    def run_move(self, move: Move) -> None:
        n = self.next(self.robot, move)
        match self[n]:
            case Cell.SPACE:
                self[n] = Cell.ROBOT
                self[self.robot] = Cell.SPACE
                self.robot = n
            case Cell.WALL:
                pass
            case Cell.BOX:
                self.push_boxes(n, move)
            case Cell.LEFT_BOX | Cell.RIGHT_BOX:
                self.push_wide_boxes(n, move)
            case _:
                raise ValueError(f"Unknown cell type {self[n]!r} at {n}")

    def push_wide_boxes(self, first_box: utils.Coord, move: Move) -> None:
        match move:
            case Move.LEFT | Move.RIGHT:
                self.push_boxes(first_box, move)
            case Move.UP | Move.DOWN:
                self.push_wide_boxes_vertically(first_box, move)

    def push_boxes(self, first_box: utils.Coord, move: Move) -> None:
        if not self.can_push_boxes(first_box, move):
            return
        value = Cell.SPACE
        c = self.robot
        while self[c] != Cell.SPACE:
            tmp = self[c]
            self[c] = value
            value = tmp
            c = self.next(c, move)
        self[c] = value
        self.robot = first_box

    def can_push_boxes(self, first_box: utils.Coord, move: Move) -> bool:
        boxes = [Cell.BOX, Cell.LEFT_BOX, Cell.RIGHT_BOX]
        next_box = first_box
        while self[next_box] in boxes:
            next_box = self.next(next_box, move)
            match self[next_box]:
                case Cell.SPACE:
                    return True
                case Cell.WALL:
                    return False
                case Cell.BOX | Cell.LEFT_BOX | Cell.RIGHT_BOX:
                    pass
                case _:
                    raise ValueError(
                        f"Unknown cell type {self[next_box]!r} at {next_box}"
                    )
        return False

    def can_push_wide_boxes(self, first_box: utils.Coord, move: Move) -> bool:
        next_coords = self.affected(first_box)
        while all(self[c] != Cell.WALL for c in next_coords):
            next_coords = self.next_affected(next_coords, move)
            if all(self[c] == Cell.SPACE for c in next_coords):
                return True
            next_coords = {c for c in next_coords if self[c] != Cell.SPACE}
        return False

    def push_wide_boxes_vertically(self, first_box: utils.Coord, move: Move) -> None:
        if not self.can_push_wide_boxes(first_box, move):
            return
        cs = self.affected(first_box)
        values = {c: Cell.SPACE for c in cs}
        while not all(self[c] == Cell.SPACE for c in cs):
            tmp = {c: self[c] for c in cs}
            for c, value in values.items():
                self[c] = value
            values = {self.next(c, move): v for c, v in tmp.items()}
            cs = {c for c in self.next_affected(cs, move) if self[c] != Cell.SPACE}
            values.update({c: Cell.SPACE for c in cs if c not in values})
        for c, value in values.items():
            self[c] = value
        self[self.robot] = Cell.SPACE
        self.robot = self.next(self.robot, move)
        self[self.robot] = Cell.ROBOT

    def next_affected(self, coords: set[utils.Coord], move: Move) -> set[utils.Coord]:
        result: set[utils.Coord] = set()
        for c in coords:
            result |= self.affected(self.next(c, move))
        return result

    def affected(self, coord: utils.Coord) -> set[utils.Coord]:
        match self[coord]:
            case Cell.LEFT_BOX:
                return {coord, utils.add_coord(coord, (0, 1))}
            case Cell.RIGHT_BOX:
                return {coord, utils.add_coord(coord, (0, -1))}
            case _:
                return {coord}

    def next(self, coord: utils.Coord, move: Move) -> utils.Coord:
        match move:
            case Move.UP:
                return utils.add_coord(coord, (-1, 0))
            case Move.RIGHT:
                return utils.add_coord(coord, (0, 1))
            case Move.DOWN:
                return utils.add_coord(coord, (1, 0))
            case Move.LEFT:
                return utils.add_coord(coord, (0, -1))


def parse_input(lines: list[str]) -> tuple[Warehouse, list[Move]]:
    warehouse_lines, moves_lines = utils.split_by_empty_lines(lines)
    warehouse = Warehouse([[Cell(c) for c in line] for line in warehouse_lines])
    moves = [Move(c) for c in "".join(moves_lines)]
    return warehouse, moves


def main() -> None:
    warehouse1, moves = parse_input(utils.read_input_lines(__file__))
    warehouse2 = warehouse1.widen()
    print(warehouse1.sum_boxes_coordinates_after_moves(moves))
    print(warehouse2.sum_boxes_coordinates_after_moves(moves))


if __name__ == "__main__":
    main()
