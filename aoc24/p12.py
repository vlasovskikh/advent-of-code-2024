import collections
from aoc24 import utils


type Region = set[utils.Coord]

CROSS_STEPS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Garden(utils.Grid[str]):
    def total_fencing_price(self) -> int:
        regions = self.regions()
        return sum(len(r) * len(self.perimeter(r, CROSS_STEPS)) for r in regions)

    def total_price_with_discount(self) -> int:
        regions = self.regions()
        return sum(len(r) * self.count_sides(r) for r in regions)

    def regions(self) -> list[Region]:
        visited: set[utils.Coord] = set()
        result: list[Region] = []
        for coord in self:
            if coord in visited:
                continue
            result.append(self.find_region(coord, visited=visited))
        return result

    def find_region(self, coord: utils.Coord, *, visited: set[utils.Coord]) -> Region:
        result: Region = set()
        stack = [coord]
        plant = self[coord]
        while stack:
            c = stack.pop()
            if c in visited:
                continue
            visited.add(c)
            result.add(c)
            for step in CROSS_STEPS:
                n = utils.add_coord(c, step)
                if n in self and self[n] == plant:
                    stack.append(n)
        return result

    def perimeter(
        self,
        region: Region,
        steps: list[utils.Coord],
    ) -> list[utils.Coord]:
        result: list[utils.Coord] = []
        for c in region:
            for step in steps:
                n = utils.add_coord(c, step)
                if n not in self or self[n] != self[c]:
                    result.append(n)
        return result

    def count_sides(self, region: Region) -> int:
        result = 0
        for step in CROSS_STEPS:
            horizontal_step = step[0] == 0
            perimeter = self.perimeter(region, [step])
            indexes: dict[int, list[int]] = collections.defaultdict(list)
            for line, column in perimeter:
                k, v = (column, line) if horizontal_step else (line, column)
                indexes[k].append(v)
            for value in indexes.values():
                result += count_segments(value)
        return result


def count_segments(xs: list[int]) -> int:
    xs = sorted(xs)
    if len(xs) <= 1:
        return len(xs)
    result = 1
    for prev, cur in utils.sliding_window(xs, 2):
        if cur != prev and cur != prev + 1:
            result += 1
    return result


def parse_input(lines: list[str]) -> Garden:
    return Garden([list(line) for line in lines])


def main() -> None:
    garden = parse_input(utils.read_input_lines(__file__))
    print(garden.total_fencing_price())
    print(garden.total_price_with_discount())


if __name__ == "__main__":
    main()
