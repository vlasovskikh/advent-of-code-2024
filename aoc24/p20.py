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

    def count_cheats(self) -> dict[int, int]:
        cheats: set[Cheat] = set()
        for c in self:
            if self[c] != Cell.WALL:
                cheats |= self.coord_cheats(c)
        paths = self.all_shortest_paths()
        savings = [s for cheat in cheats if (s := self.saving(cheat, paths)) > 0]
        return collections.Counter(savings)

    def count_cheats_gte_100(self) -> int:
        cheats = self.count_cheats()
        return sum(count for saving, count in cheats.items() if saving >= 100)

    def coord_cheats(self, coord: utils.Coord) -> set[Cheat]:
        cheats = [
            utils.add_coord(coord, (0, 2)),
            utils.add_coord(coord, (0, -2)),
            utils.add_coord(coord, (2, 0)),
            utils.add_coord(coord, (-2, 0)),
        ]
        return {(coord, c) for c in cheats if c in self and self[c] != Cell.WALL}

    def saving(self, cheat: Cheat, paths: dict[utils.Coord, int]) -> int:
        start, end = cheat
        result = paths[end] - paths[start] - 2  # Cheat length
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


def parse_input(lines: list[str]) -> Track:
    return Track([[Cell(c) for c in line] for line in lines])


def main() -> None:
    track = parse_input(utils.read_input_lines(__file__))
    print(track.count_cheats_gte_100())


if __name__ == "__main__":
    main()
