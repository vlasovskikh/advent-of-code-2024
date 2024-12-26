import collections
from aoc24 import utils


def sum_predicted_secrets(secrets: list[int]) -> int:
    return sum(predict_secret(s, 2000) for s in secrets)


def sum_best_prices(secrets: list[int]) -> int:
    indexes: list[dict[tuple[int, ...], int]] = []
    for secret in secrets:
        steps = list_secrets(secret, 2000)
        indexes.append(index_scores(steps))

    same_key: dict[tuple[int, ...], list[int]] = collections.defaultdict(list)
    for i, index in enumerate(indexes):
        for k in index:
            same_key[k].append(i)

    best_prices = 0
    for k, ii in same_key.items():
        prices = [indexes[i][k] for i in ii]
        total_price = sum(prices)
        if total_price > best_prices:
            best_prices = total_price

    return best_prices


def index_scores(steps: list[int]) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    prices = [int(str(x)[-1]) for x in steps]
    for i in range(len(prices) - 5):
        ps = prices[i : i + 5]
        changes = tuple([ps[i + 1] - ps[i] for i in range(len(ps) - 1)])
        if changes not in result:
            result[changes] = ps[-1]
    return result


def predict_secret(secret: int, steps: int) -> int:
    return list_secrets(secret, steps)[-1]


def list_secrets(secret: int, steps: int) -> list[int]:
    results = [secret]
    for _ in range(steps):
        secret = evolve(secret)
        results.append(secret)
    return results


def evolve(secret: int) -> int:
    s1 = ((secret * 64) ^ secret) % 16777216
    s2 = ((s1 // 32) ^ s1) % 16777216
    s3 = ((s2 * 2048) ^ s2) % 16777216
    return s3


def parse_input(lines: list[str]) -> list[int]:
    return [int(line) for line in lines]


def main() -> None:
    secrets = parse_input(utils.read_input_lines(__file__))
    print(sum_predicted_secrets(secrets))
    print(sum_best_prices(secrets))


if __name__ == "__main__":
    main()
