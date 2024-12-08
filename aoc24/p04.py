import typing

from aoc24 import utils


class WordGrid(utils.Grid[str]):
    def extrapolate(self, x1: utils.Coord, x2: utils.Coord) -> utils.Coord | None:
        diff = utils.sub_coord(x2, x1)
        x3 = utils.add_coord(x2, diff)
        return x3 if x3 in self else None


def count_xmas(grid: WordGrid) -> int:
    count = 0
    for x in grid:
        if grid[x] != "X":
            continue
        for m in grid.neighbors(x):
            if grid[m] != "M":
                continue
            a = grid.extrapolate(x, m)
            if a is None or grid[a] != "A":
                continue
            s = grid.extrapolate(m, a)
            if s is not None and grid[s] == "S":
                count += 1
    return count


def count_x_mas(grid: WordGrid) -> int:
    count = 0
    for a in grid:
        if grid[a] != "A":
            continue
        ds = grid.diagonal_neighbors(a)
        chars = sorted(grid[d] for d in ds)
        if chars != ["M", "M", "S", "S"]:
            continue
        for m in ds:
            if grid[m] != "M":
                continue
            s = grid.extrapolate(m, a)
            if s is not None and grid[s] == "S":
                count += 1
                break
    return count


def parse_input(lines: typing.Sequence[str]) -> WordGrid:
    return WordGrid([list(line) for line in lines])


def main() -> None:
    grid = parse_input(utils.read_input_lines(__file__))
    print(count_xmas(grid))
    print(count_x_mas(grid))


if __name__ == "__main__":
    main()
