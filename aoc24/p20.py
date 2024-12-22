import collections
import enum
import heapq
from aoc24 import utils


class Cell(enum.StrEnum):
    SPACE = "."
    WALL = "#"
    START = "S"
    END = "E"


type Cheat = tuple[utils.Coord, utils.Coord]


class Track(utils.Grid[Cell]):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.start = next(c for c in self if self[c] == Cell.START)
        self.end = next(c for c in self if self[c] == Cell.END)

    def count_cheats(self, distance: int) -> dict[int, int]:
        cheats: set[Cheat] = set()
        for c in self:
            if self[c] != Cell.WALL:
                cheats |= self.coord_cheats(c, distance)
        paths = self.all_shortest_paths()
        savings = [s for cheat in cheats if (s := self.saving(cheat, paths)) > 0]
        return collections.Counter(savings)

    def count_cheats_gte_100(self, distance: int) -> int:
        cheats = self.count_cheats(distance)
        return sum(count for saving, count in cheats.items() if saving >= 100)

    def coord_cheats(self, start: utils.Coord, distance: int) -> set[Cheat]:
        """Find all cheat coordinates not farther than `distance`."""
        sx, sy = start
        cheats: set[Cheat] = set()
        for x in range(sx - distance, sx + distance + 1):
            for y in range(sy - distance, sy + distance + 1):
                end = x, y
                if (
                    end != start
                    and end in self
                    and coord_distance(start, end) <= distance
                    and self[end] != Cell.WALL
                ):
                    cheats.add((start, end))
        return cheats

    def saving(self, cheat: Cheat, paths: dict[utils.Coord, int]) -> int:
        start, end = cheat
        result = paths[end] - paths[start] - coord_distance(start, end)
        return result

    def all_shortest_paths(self) -> dict[utils.Coord, int]:
        best_score: dict[utils.Coord, int] = {}
        heap: list[tuple[int, utils.Coord]] = []
        heapq.heappush(heap, (0, self.start))

        while heap:
            score, coord = heapq.heappop(heap)
            if coord in best_score:
                continue
            best_score[coord] = score
            for n in self.cross_neighbors(coord):
                if self[n] != Cell.WALL:
                    heapq.heappush(heap, (score + 1, n))

        return best_score


def coord_distance(c1: utils.Coord, c2: utils.Coord) -> int:
    dx, dy = utils.sub_coord(c1, c2)
    return abs(dx) + abs(dy)


def parse_input(lines: list[str]) -> Track:
    return Track([[Cell(c) for c in line] for line in lines])


def main() -> None:
    track = parse_input(utils.read_input_lines(__file__))
    print(track.count_cheats_gte_100(2))
    print(track.count_cheats_gte_100(20))


if __name__ == "__main__":
    main()
