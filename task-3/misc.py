from typing import TypedDict


class LogEntry(TypedDict):
    date: str
    time: str
    level: str
    message: str
