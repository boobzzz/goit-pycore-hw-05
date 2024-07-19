from typing import List, Dict
from user_data import users
from decorators import input_error
from commands import Commands
from utils import normalize_phone


def get_response(cmd: str, args: List):
    response = None
    match cmd:
        case Commands.HELLO:
            response = Commands.messages.get(Commands.HELLO)
        case Commands.ADD:
            response = add_contact(args)
        case Commands.CHANGE:
            response = change_contact(args)
        case Commands.PHONE:
            response = show_phone(args)
        case Commands.ALL:
            response = show_all()
    return response


@input_error
def add_contact(args: List) -> str:
    user_name, user_phone = args
    norm_phone = normalize_phone(user_phone)

    if user_name in users:
        raise ValueError(Commands.errors.get(Commands.USER_EXISTS))
    if not norm_phone:
        raise ValueError(Commands.errors.get(Commands.PHONE_INVALID))

    users[user_name] = norm_phone
    return Commands.messages.get(Commands.ADD)


@input_error
def change_contact(args: List) -> str:
    user_name, user_phone = args
    norm_phone = normalize_phone(user_phone)

    if user_name not in users:
        raise ValueError(Commands.errors.get(Commands.USER_NOT_EXISTS))
    if not norm_phone:
        raise ValueError(Commands.errors.get(Commands.PHONE_INVALID))

    users[user_name] = norm_phone
    return Commands.messages.get(Commands.CHANGE)


@input_error
def show_phone(args: List) -> str:
    user_name = args[0]

    if user_name not in users:
        raise ValueError(Commands.errors.get(Commands.USER_NOT_EXISTS))

    return users.get(user_name)


def show_all() -> Dict:
    return users
