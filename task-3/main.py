import sys
from typing import List, Tuple
from handler import load_logs, filter_logs_by_level, count_logs_by_level


def parse_cmd_line(sys_args: List[str]) -> Tuple[str, str]:
    path = ""
    level = ""
    if len(sys_args) >= 2:
        path = sys_args[1]
    if len(sys_args) == 3:
        level = sys_args[2]

    return path, level


def main():
    path, level = parse_cmd_line(sys.argv)
    logs = load_logs(path)

    if logs:
        count_logs_by_level(logs)
        if level:
            filter_logs_by_level(logs, level)


if __name__ == "__main__":
    main()
