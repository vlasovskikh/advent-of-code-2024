from aoc24 import utils
from collections import Counter


def total_distance(xs: list[int], ys: list[int]) -> int:
    return sum(abs(x - y) for x, y in zip(sorted(xs), sorted(ys)))


def similarity_score(xs: list[int], ys: list[int]) -> int:
    cnt: dict[int, int] = Counter(ys)
    return sum(x * cnt[x] for x in xs if x in cnt)


def parse_input(lines: list[str]) -> tuple[list[int], list[int]]:
    xs: list[int] = []
    ys: list[int] = []
    for line in lines:
        x, y = line.split()
        xs.append(int(x))
        ys.append(int(y))
    return xs, ys


def main() -> None:
    xs, ys = parse_input(utils.read_input_lines(__file__))
    print(total_distance(xs, ys))
    print(similarity_score(xs, ys))


if __name__ == "__main__":
    main()
