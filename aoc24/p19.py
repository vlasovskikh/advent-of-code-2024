import functools

from aoc24 import utils


type State = tuple[str, int]
type Range = tuple[int, int]


def count_possible_designs(
    designs: list[str], *, patterns: list[str]
) -> tuple[int, int]:
    paths = [design_arrangements(d, patterns) for d in designs]
    return len([p for p in paths if p > 0]), sum(paths)


def design_arrangements(design: str, patterns: list[str]) -> int:
    patterns_set = frozenset(patterns)
    states = init_states(patterns_set)
    matched: set[Range] = set()
    for i, c in enumerate(design):
        states, finished = transitions(c, states, patterns_set)
        if not states:
            return 0
        for towel in finished:
            start = i - (len(towel) - 1)
            matched.add((start, start + len(towel)))
    return count_paths(0, len(design), frozenset(matched))


@functools.cache
def count_paths(start: int, stop: int, ranges: frozenset[Range]) -> int:
    if start == stop:
        return 1
    next_ranges = [r for r in ranges if r[0] == start]
    if len(next_ranges) == 0:
        return 0
    elif len(next_ranges) == 1:
        r = next_ranges[0]
        return count_paths(r[1], stop, ranges)
    else:
        result = 0
        for r in next_ranges:
            result += count_paths(r[1], stop, ranges)
        return result


@functools.cache
def init_states(patterns: frozenset[str]) -> frozenset[State]:
    return frozenset((pattern, 0) for pattern in patterns)


@functools.cache
def transitions(
    c: str, states: frozenset[State], patterns: frozenset[str]
) -> tuple[frozenset[State], frozenset[str]]:
    result: set[State] = set()
    all_finished: set[str] = set()
    for state in states:
        new_states, finished = transition(c, state, patterns)
        result |= new_states
        all_finished |= finished
    return frozenset(result), frozenset(all_finished)


def transition(
    c: str, state: State, patterns: frozenset[str]
) -> tuple[frozenset[State], frozenset[str]]:
    towel, i = state
    if i >= len(towel) or i < 0:
        raise ValueError(f"Incorrect state: {state!r}")
    if c != towel[i]:
        return frozenset(), frozenset()
    if i == len(towel) - 1:
        return init_states(patterns), frozenset({towel})
    return frozenset({(towel, i + 1)}), frozenset()


def parse_input(lines: list[str]) -> tuple[list[str], list[str]]:
    patterns_lines, designs = utils.split_by_empty_lines(lines)
    assert len(patterns_lines) == 1
    patterns = patterns_lines[0].split(", ")
    return designs, patterns


def main() -> None:
    designs, patterns = parse_input(utils.read_input_lines(__file__))
    possible, paths = count_possible_designs(designs, patterns=patterns)
    print(possible)
    print(paths)


if __name__ == "__main__":
    main()
