from aoc24 import p05


def test_example_1() -> None:
    lines = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip().splitlines()
    rules, updates = p05.parse_input(lines)
    assert p05.sum_middle_pages_from_correct_updates(rules, updates) == 143


def test_example_2() -> None:
    lines = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip().splitlines()
    rules, updates = p05.parse_input(lines)
    assert p05.sum_middle_pages_from_incorrect_updates(rules, updates) == 123
