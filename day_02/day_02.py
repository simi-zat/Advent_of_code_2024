from enum import Enum, auto


class ReportStatus(Enum):
    NOT_SAFE = auto()
    SAFE = auto()
    SAFE_WITH_DEFECT = auto()


def get_report_status(report: list[int]) -> ReportStatus:
    diff = [report[r] - report[r + 1] for r in range(len(report) - 1)]

    if all([1 <= x <= 3 for x in diff]) or all([-3 <= x <= -1 for x in diff]):
        return ReportStatus.SAFE

    else:
        for tmp_idx in range(len(report)):
            tmp_report = report[0:tmp_idx] + report[tmp_idx + 1:]
            tmp_diff = [tmp_report[tr] - tmp_report[tr + 1] for tr in range(len(tmp_report) - 1)]

            if all([1 <= tx <= 3 for tx in tmp_diff]) or all([-3 <= tx <= -1 for tx in tmp_diff]):
                return ReportStatus.SAFE_WITH_DEFECT

    return ReportStatus.NOT_SAFE


if __name__ == '__main__':
    input_data = "data_challenge.in"

    safe_reports: int = 0
    safe_reports_with_defects: int = 0

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            rep = get_report_status([int(x) for x in line.split()])

            if rep == ReportStatus.SAFE:
                safe_reports += 1

            elif rep == ReportStatus.SAFE_WITH_DEFECT:
                safe_reports_with_defects += 1

    print("\n-- Part 1: --")
    print(safe_reports)
    print("\n-- Part 2: --")
    print(safe_reports + safe_reports_with_defects)
