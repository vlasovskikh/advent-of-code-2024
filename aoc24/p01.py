from aoc24 import utils


def total_distance(xs: list[int], ys: list[int]) -> int:
    return sum(abs(x - y) for x, y in zip(sorted(xs), sorted(ys)))


def similarity_score(xs: list[int], ys: list[int]) -> int:
    cnt: dict[int, int] = {}
    for y in ys:
        if y in cnt:
            cnt[y] += 1
        else:
            cnt[y] = 1
    s = 0
    for x in xs:
        if x in cnt:
            s += x * cnt[x]
    return s


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
