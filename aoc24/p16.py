import collections
import enum
import heapq

from aoc24 import utils


class Cell(enum.StrEnum):
    SPACE = "."
    WALL = "#"
    START = "S"
    END = "E"
    SEAT = "O"


type Pos = tuple[utils.Coord, utils.Dir]


class Maze(utils.Grid[Cell]):
    def shortest_path(self) -> tuple[int, int]:
        start = next(c for c in self if self[c] == Cell.START)
        end = next(c for c in self if self[c] == Cell.END)
        start_pos = start, utils.Dir.RIGHT
        heap: list[tuple[int, Pos, Pos]] = [(0, start_pos, start_pos)]
        best_score: dict[Pos, int] = {}
        traceback: dict[Pos, set[Pos]] = collections.defaultdict(set)

        while heap:
            score, pos, prev = heapq.heappop(heap)
            coord, direction = pos
            if pos in best_score and score > best_score[pos]:
                continue
            if prev != pos:
                traceback[pos].add(prev)
            if pos in best_score and score == best_score[pos]:
                continue
            best_score[pos] = score
            if self[coord] == Cell.END:
                continue
            heapq.heappush(heap, (score + 1000, (coord, direction.turn270), pos))
            heapq.heappush(heap, (score + 1000, (coord, direction.turn90), pos))
            next_coord = self.next(coord, direction)
            if self[next_coord] != Cell.WALL:
                heapq.heappush(heap, (score + 1, (next_coord, direction), pos))

        min_score = min(
            [best_score[(end, d)] for d in utils.Dir if (end, d) in best_score]
        )
        stack: list[Pos] = [
            (end, d) for d in utils.Dir if best_score.get((end, d)) == min_score
        ]
        coords: set[utils.Coord] = set()
        while stack:
            pos = stack.pop()
            if pos[0] not in coords:
                self[pos[0]] = Cell.SEAT
            coords.add(pos[0])
            if pos in traceback:
                for prev in traceback[pos]:
                    stack.append(prev)

        return min_score, len(coords)

    def next(self, coord: utils.Coord, direction: utils.Dir) -> utils.Coord:
        match direction:
            case utils.Dir.UP:
                diff = -1, 0
            case utils.Dir.RIGHT:
                diff = 0, 1
            case utils.Dir.DOWN:
                diff = 1, 0
            case utils.Dir.LEFT:
                diff = 0, -1
        return utils.add_coord(coord, diff)


def parse_input(lines: list[str]) -> Maze:
    return Maze([[Cell(c) for c in line] for line in lines])


def main() -> None:
    maze = parse_input(utils.read_input_lines(__file__))
    score, seats = maze.shortest_path()
    print(score)
    print(seats)


if __name__ == "__main__":
    main()
