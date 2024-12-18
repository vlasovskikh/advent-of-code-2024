from __future__ import annotations
import bisect
import dataclasses
import enum
import heapq
from aoc24 import utils


class Cell(enum.StrEnum):
    SAFE = "."
    CORRUPTED = "#"


class MemorySpace(utils.Grid[Cell]):
    def shortest_path(self) -> int | None:
        start = (0, 0)
        stop = utils.sub_coord(self.size(), (1, 1))
        best_score: dict[utils.Coord, int] = {}
        heap: list[tuple[int, utils.Coord]] = []
        heapq.heappush(heap, (0, start))

        while heap:
            score, coord = heapq.heappop(heap)
            if coord == stop:
                return score
            if coord in best_score and score >= best_score[coord]:
                continue
            best_score[coord] = score
            for n in self.cross_neighbors(coord):
                if self[n] != Cell.CORRUPTED:
                    heapq.heappush(heap, (score + 1, n))

        return None

    @staticmethod
    def create(size: utils.Coord, coords: list[utils.Coord]) -> MemorySpace:
        size_x, size_y = size
        memory = MemorySpace(
            [[Cell.SAFE for _ in range(size_y)] for _ in range(size_x)]
        )
        for c in coords:
            memory[c] = Cell.CORRUPTED
        return memory


@dataclasses.dataclass
class Path:
    size: utils.Coord
    coords: list[utils.Coord]


def shortest_path(*, size: utils.Coord, coords: list[utils.Coord]) -> int | None:
    return MemorySpace.create(size, coords).shortest_path()


def bisect_key(path: Path) -> bool:
    """Returns False when there is a path and True if there is no path."""
    return shortest_path(size=path.size, coords=path.coords) is None


def first_blocking_coord(*, size: utils.Coord, coords: list[utils.Coord]) -> str:
    paths = [Path(size=size, coords=coords[: i + 1]) for i in range(len(coords))]
    i = bisect.bisect_left(paths, True, key=bisect_key)
    if i > 0:
        x, y = coords[i]
        return f"{x},{y}"
    else:
        raise ValueError("No coord ever blocks a path from start to end")


def parse_input(lines: list[str]) -> list[utils.Coord]:
    result: list[utils.Coord] = []
    for line in lines:
        x, y = line.split(",")
        result.append((int(x), int(y)))
    return result


def main() -> None:
    coords = parse_input(utils.read_input_lines(__file__))
    print(shortest_path(size=(71, 71), coords=coords[:1024]))
    print(first_blocking_coord(size=(71, 71), coords=coords))


if __name__ == "__main__":
    main()
