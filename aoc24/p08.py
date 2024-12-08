import itertools
import collections

from aoc24 import utils


class Grid(utils.Grid[str]):
    def antenna_groups(self) -> list[list[utils.Coord]]:
        groups: dict[str, list[utils.Coord]] = collections.defaultdict(list)
        for coord in self:
            value = self[coord]
            if value == ".":
                continue
            groups[value].append(coord)
        return list(groups.values())

    def antinodes(self, a1: utils.Coord, a2: utils.Coord) -> set[utils.Coord]:
        diff = utils.sub_coord(a1, a2)
        candidates = {utils.add_coord(a1, diff), utils.sub_coord(a2, diff)}
        return {c for c in candidates if c in self}

    def resonant_antinodes(self, a1: utils.Coord, a2: utils.Coord) -> set[utils.Coord]:
        result: set[utils.Coord] = set()
        diff = utils.sub_coord(a1, a2)
        c = a1
        while c in self:
            result.add(c)
            c = utils.add_coord(c, diff)
        c = a2
        while c in self:
            result.add(c)
            c = utils.sub_coord(c, diff)
        return result

    def count_antinodes(self, *, resonant: bool) -> int:
        antinodes: set[utils.Coord] = set()
        for group in self.antenna_groups():
            for a1, a2 in itertools.combinations(group, 2):
                antinodes |= (
                    self.resonant_antinodes(a1, a2)
                    if resonant
                    else self.antinodes(a1, a2)
                )
        return len(antinodes)


def parse_input(lines: list[str]) -> Grid:
    return Grid([list(line) for line in lines])


def main() -> None:
    grid = parse_input(utils.read_input_lines(__file__))
    print(grid.count_antinodes(resonant=False))
    print(grid.count_antinodes(resonant=True))


if __name__ == "__main__":
    main()
