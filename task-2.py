from typing import Callable, Iterable

income_text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений "
               "додатковими надходженнями 27.45 і 324.00 доларів.")


def generator_numbers(text: str) -> Iterable:
    for phrase in text.split(" "):
        if phrase.replace(".", "").isnumeric():
            yield float(phrase)


def sum_profit(text: str, generator: Callable[[str], Iterable]) -> float:
    total = 0.0
    for num in generator(text):
        total += num

    return total


total_income = sum_profit(income_text, generator_numbers)
print(f"Загальний дохід: {total_income}")
