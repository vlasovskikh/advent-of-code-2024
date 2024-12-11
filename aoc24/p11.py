import collections
import functools

from aoc24 import utils


def count_changed_stones(stones: list[int], steps: int) -> int:
    return sum(changed_stones(stones, steps).values())


def changed_stones(stones: list[int], steps: int) -> dict[int, int]:
    result: dict[int, int] = collections.defaultdict(int)
    for stone in stones:
        res = changed_stone(stone, steps)
        for k, v in res.items():
            result[k] += v
    return result


@functools.cache
def changed_stone(stone: int, steps: int) -> dict[int, int]:
    result: dict[int, int] = collections.defaultdict(int)
    if steps == 1:
        if stone == 0:
            result[1] += 1
        elif len(s := str(stone)) % 2 == 0:
            half = len(s) // 2
            result[int(s[:half])] += 1
            result[int(s[half:])] += 1
        else:
            result[stone * 2024] += 1
    else:
        for prev_stone, prev_count in changed_stone(stone, steps - 1).items():
            for cur_stone, cur_count in changed_stone(prev_stone, 1).items():
                result[cur_stone] += cur_count * prev_count
    return result


def parse_input(lines: list[str]) -> list[int]:
    assert len(lines) == 1
    return [int(s) for s in lines[0].split()]


def main() -> None:
    stones = parse_input(utils.read_input_lines(__file__))
    print(count_changed_stones(stones, 25))
    print(count_changed_stones(stones, 75))


if __name__ == "__main__":
    main()
