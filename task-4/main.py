from typing import Tuple
from commands import Commands
from handler import get_response


def parse_input(user_input: str) -> Tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to the assistant bot!")
    while True:
        cmd, *args = parse_input(input("Enter a command: "))
        if cmd in [Commands.EXIT, Commands.CLOSE]:
            print(Commands.messages[Commands.EXIT])
            break

        if cmd in list(Commands.messages.keys()):
            print(get_response(cmd, args))
        else:
            print(Commands.messages[Commands.INVALID])


if __name__ == "__main__":
    main()
