from aoc24 import p22


def test_example_1() -> None:
    lines = """
1
10
100
2024
""".strip().splitlines()
    secrets = p22.parse_input(lines)
    assert p22.sum_predicted_secrets(secrets) == 37327623


def test_next_10_secrets() -> None:
    assert p22.list_secrets(123, 10) == [
        123,
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]


def test_example_2() -> None:
    lines = """
1
2
3
2024
""".strip().splitlines()
    secrets = p22.parse_input(lines)
    assert p22.sum_best_prices(secrets) == 23
