from __future__ import annotations
import collections
import dataclasses
import math
import re
import sys
from aoc24 import utils


@dataclasses.dataclass
class Robot:
    p: utils.Coord
    v: utils.Coord

    def move(self, area: Area, seconds: int) -> Robot:
        assert area.start == (0, 0)
        moved = (
            (self.p[0] + self.v[0] * seconds) % area.stop[0],
            (self.p[1] + self.v[1] * seconds) % area.stop[1],
        )
        return Robot(p=moved, v=self.v)


@dataclasses.dataclass
class Area:
    start: utils.Coord
    stop: utils.Coord

    def quadrants(self) -> list[Area]:
        half: utils.Coord = (
            self.start[0] + (self.stop[0] - self.start[0]) // 2,
            self.start[1] + (self.stop[1] - self.start[1]) // 2,
        )
        return [
            Area(self.start, half),
            Area((half[0] + 1, self.start[1]), (self.stop[0], half[1])),
            Area((self.start[0], half[1] + 1), (half[0], self.stop[1])),
            Area((half[0] + 1, half[1] + 1), self.stop),
        ]

    def __contains__(self, coord: utils.Coord) -> bool:
        return (
            self.start[0] <= coord[0] < self.stop[0]
            and self.start[1] <= coord[1] < self.stop[1]
        )

    def show(self, robots: list[Robot]) -> None:
        field: list[list[str]] = [
            ["." for _ in range(self.stop[0])] for _ in range(0, self.stop[1])
        ]
        for robot in robots:
            field[robot.p[1]][robot.p[0]] = "#"
        print("\n".join("".join(line) for line in field))


def safety_factor(robots: list[Robot], *, size: utils.Coord, seconds: int) -> int:
    area = Area(start=(0, 0), stop=size)
    moved = [robot.move(area, seconds) for robot in robots]
    quadrants = area.quadrants()
    result: dict[int, int] = collections.defaultdict(int)
    for i, quadrant in enumerate(quadrants):
        for robot in moved:
            if robot.p in quadrant:
                result[i] += 1
    return math.prod(result.values())


def parse_input(lines: list[str]) -> list[Robot]:
    result: list[Robot] = []
    for line in lines:
        m = re.match(r"p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)", line)
        if not m:
            raise ValueError(f"Unknown line: {line!r}")
        result.append(
            Robot(
                p=(int(m.group(1)), int(m.group(2))),
                v=(int(m.group(3)), int(m.group(4))),
            )
        )
    return result


def visualize(robots: list[Robot], *, size: utils.Coord, seconds: int) -> None:
    area = Area((0, 0), size)
    # It's the first insteresting not quite random combination
    next_guess = 4
    for i in range(seconds):
        if i == next_guess:
            # These interesting combinations keep showing up every 101 seconds
            next_guess = i + 101
            print(f"Step {i}")
            area.show(robots)
            input()
        robots = [robot.move(area, 1) for robot in robots]


def main() -> None:
    robots = parse_input(utils.read_input_lines(__file__))
    if len(sys.argv) == 2 and sys.argv[1] == "show":
        visualize(robots, size=(101, 103), seconds=1_000_000)
    else:
        print(safety_factor(robots, size=(101, 103), seconds=100))


if __name__ == "__main__":
    main()
