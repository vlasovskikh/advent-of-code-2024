import itertools

from aoc24 import utils


type Lock = list[int]
type Key = list[int]


def count_fitting(locks: list[Lock], keys: list[Key]) -> int:
    result = 0
    for lock, key in itertools.product(locks, keys):
        if fit(lock, key):
            result += 1
    return result


def fit(lock: Lock, key: Key) -> bool:
    return all(x + y <= 5 for x, y in zip(lock, key))


class Schematic(utils.Grid[str]):
    def is_lock(self) -> bool:
        return all(c == "#" for c in self.data[0])

    def to_sequence(self) -> list[int]:
        result: list[int] = []
        lines, columns = self.size
        for j in range(columns):
            count = 0
            for i in range(lines):
                if self.data[i][j] == "#":
                    count += 1
            result.append(count - 1)
        return result


def parse_input(lines: list[str]) -> tuple[list[Lock], list[Key]]:
    locks: list[Lock] = []
    keys: list[Key] = []
    for group in utils.split_by_empty_lines(lines):
        s = Schematic([list(line) for line in group])
        collection = locks if s.is_lock() else keys
        collection.append(s.to_sequence())
    return locks, keys


def main() -> None:
    locks, keys = parse_input(utils.read_input_lines(__file__))
    print(count_fitting(locks, keys))


if __name__ == "__main__":
    main()
