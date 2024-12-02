from typing import Sequence, Iterator

from aoc24 import utils


def safe_reports_count(reports: list[list[int]]) -> int:
    return sum(int(is_safe_report(report)) for report in reports)


def tolerant_safe_reports_count(reports: list[list[int]]) -> int:
    return sum(
        int(
            is_safe_report(report)
            or any(is_safe_report(r) for r in all_reports_without_one_level(report))
        )
        for report in reports
    )


def all_reports_without_one_level(report: list[int]) -> Iterator[list[int]]:
    for i in range(len(report)):
        c = report.copy()
        c.pop(i)
        yield c


def is_safe_report(report: list[int]) -> bool:
    diffs = report_diff(report)
    return all(1 <= diff <= 3 for diff in diffs) or all(
        -3 <= diff <= -1 for diff in diffs
    )


def report_diff(report: list[int]) -> list[int]:
    pairs = utils.sliding_window(report, 2)
    return [y - x for x, y in pairs]


def parse_input(lines: Sequence[str]) -> list[list[int]]:
    return [[int(s) for s in line.split()] for line in lines]


def main() -> None:
    reports = parse_input(utils.read_input_lines(__file__))
    print(safe_reports_count(reports))
    print(tolerant_safe_reports_count(reports))


if __name__ == "__main__":
    main()
