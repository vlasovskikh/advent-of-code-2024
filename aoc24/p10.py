from aoc24 import utils


class Grid(utils.Grid[int]):
    def sum_trailhead_scores(self, *, by_rating: bool) -> int:
        trails = [
            self.count_hiking_trails(c, by_rating=by_rating) for c in self.trailheads()
        ]
        return sum(trails)

    def trailheads(self) -> list[utils.Coord]:
        return [c for c in self if self[c] == 0]

    def count_hiking_trails(self, trailhead: utils.Coord, *, by_rating: bool) -> int:
        stack = [trailhead]
        result = 0
        visited: set[utils.Coord] = set()
        while stack:
            c = stack.pop()
            if not by_rating:
                if c in visited:
                    continue
                visited.add(c)
            height = self[c]
            if height == 9:
                result += 1
                continue
            for n in self.cross_neighbors(c):
                if self[n] == height + 1:
                    stack.append(n)
        return result


def parse_input(lines: list[str]) -> Grid:
    return Grid([[int(c) for c in line] for line in lines])


def main() -> None:
    grid = parse_input(utils.read_input_lines(__file__))
    print(grid.sum_trailhead_scores(by_rating=False))
    print(grid.sum_trailhead_scores(by_rating=True))


if __name__ == "__main__":
    main()
