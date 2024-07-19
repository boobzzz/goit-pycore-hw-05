class Commands:
    HELLO = "hello"
    ADD = "add"
    CHANGE = "change"
    PHONE = "phone"
    ALL = "all"
    CLOSE = "close"
    EXIT = "exit"
    INVALID = "invalid"
    USER_EXISTS = "user_exists"
    USER_NOT_EXISTS = "user_not_exists"
    PHONE_INVALID = "phone_invalid"

    messages = {
        HELLO: "How can I help you?",
        ADD: "Contact added.",
        CHANGE: "Contact updated.",
        PHONE: "",
        ALL: "",
        EXIT: "Good bye!",
        INVALID: "Invalid command."
    }

    errors = {
        USER_EXISTS: "User already exists",
        USER_NOT_EXISTS: "User does not exist",
        PHONE_INVALID: "Invalid phone number format"
    }
