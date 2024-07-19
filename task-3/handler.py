from misc import LogEntry
from typing import List, Dict
from collections import namedtuple, Counter
from decorators import show_stats, show_filtered

LogLine = namedtuple('LogLine', ['date', 'time', 'level', 'message'])


def parse_log_line(line: str) -> LogEntry:
    line_to_list = LogLine(*line.split(" ", 3))
    return {
        "date": line_to_list.date,
        "time": line_to_list.time,
        "level": line_to_list.level,
        "message": line_to_list.message
    }


def load_logs(file_path: str) -> List[LogEntry]:
    lines: List[LogEntry] = []
    for line in line_reader(file_path):
        lines.append(parse_log_line(line))

    return lines


@show_filtered
def filter_logs_by_level(logs: List[LogEntry], level: str) -> List[LogEntry]:
    return [entry for entry in logs if entry['level'] == level.upper()]


@show_stats
def count_logs_by_level(logs: List[LogEntry]) -> Dict:
    levels = [entry['level'] for entry in logs]
    return Counter(levels)


def line_reader(path: str):
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()
    except OSError as e:
        print(f"{type(e)}: {e}")
