from aoc24 import p09


def test_example_1() -> None:
    lines = """
2333133121414131402
""".strip().splitlines()
    disk = p09.parse_input(lines)
    assert p09.checksum(p09.free_up_space(disk)) == 1928


def test_example_2() -> None:
    lines = """
2333133121414131402
""".strip().splitlines()
    disk = p09.parse_input(lines)
    assert p09.checksum(p09.defragment(disk)) == 2858


def test_free_up_small() -> None:
    lines = """
12345
""".strip().splitlines()
    disk = p09.parse_input(lines)
    assert "".join(str(x) for x in p09.free_up_space(disk)) == "022111222"
    assert p09.checksum(p09.free_up_space(disk)) == sum(
        i * x for i, x in enumerate(int(c) for c in "022111222")
    )


def test_defragment_small() -> None:
    lines = """
12345
""".strip().splitlines()  # 0..111....22222
    disk = p09.parse_input(lines)
    assert "".join(str(x) for x in p09.defragment(disk)) == "000111000022222"
    assert p09.checksum(p09.defragment(disk)) == sum(
        i * x for i, x in enumerate(int(c) for c in "000111000022222")
    )
