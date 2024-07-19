from typing import List, Dict
from misc import LogEntry
from functools import wraps

HEADER_LEFT = "Рівень логування"
HEADER_RIGHT = "Кількість"


def show_stats(func):
    @wraps(func)
    def inner(logs: List[Dict]) -> Dict:
        log_stats: Dict = func(logs)
        print(f"{HEADER_LEFT} | {HEADER_RIGHT}")
        print(f"{"-" * (len(HEADER_LEFT) + 1)}|{"-" * (len(HEADER_RIGHT) + 1)}")
        for log_type in log_stats.keys():
            print(f"{log_type}{" " * (len(HEADER_LEFT) - len(log_type))} | {log_stats.get(log_type)}")

        return log_stats

    return inner


def show_filtered(func):
    @wraps(func)
    def inner(logs: List[LogEntry], level: str) -> List[LogEntry]:
        log_entries: List[LogEntry] = func(logs, level)
        print(f"Деталі логів для рівня {level.upper()}:")
        for entry in log_entries:
            print(f"{entry["date"]} {entry["time"]} - {entry["message"]}")

        return log_entries

    return inner
