from collections import defaultdict

from aoc24 import utils


def is_correct_update(update: list[int], rules: dict[int, set[int]]) -> bool:
    for i, page in enumerate(update):
        after = set(update[i + 1 :])
        if after - rules[page]:
            return False
    return True


def rules_to_dict(rules: list[tuple[int, int]]) -> dict[int, set[int]]:
    rules_dict: dict[int, set[int]] = defaultdict(set)
    for k, v in rules:
        rules_dict[k].add(v)
    return rules_dict


def fix_update(update: list[int], rules: dict[int, set[int]]) -> list[int]:
    all_pages = set(update)
    not_allowed: list[tuple[int, int]] = []
    for page in all_pages:
        not_allowed.append((len(all_pages - rules[page]), page))
    not_allowed.sort()
    return [p for _, p in not_allowed]


def sum_middle_pages_from_correct_updates(
    rules: list[tuple[int, int]],
    updates: list[list[int]],
) -> int:
    rules_dict = rules_to_dict(rules)
    return sum(
        update[len(update) // 2]
        for update in updates
        if is_correct_update(update, rules_dict)
    )


def sum_middle_pages_from_incorrect_updates(
    rules: list[tuple[int, int]],
    updates: list[list[int]],
) -> int:
    rules_dict = rules_to_dict(rules)
    fixed = [
        fix_update(update, rules_dict)
        for update in updates
        if not is_correct_update(update, rules_dict)
    ]
    return sum(update[len(update) // 2] for update in fixed)


def parse_input(lines: list[str]) -> tuple[list[tuple[int, int]], list[list[int]]]:
    lines1, lines2 = utils.split_by_empty_lines(lines)
    pairs = [line.split("|") for line in lines1]
    rules = [(int(e1), int(e2)) for e1, e2 in pairs]
    updates = [[int(s) for s in line.split(",")] for line in lines2]
    return rules, updates


def main() -> None:
    rules, updates = parse_input(utils.read_input_lines(__file__))
    print(sum_middle_pages_from_correct_updates(rules, updates))
    print(sum_middle_pages_from_incorrect_updates(rules, updates))


if __name__ == "__main__":
    main()
