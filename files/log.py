from conf.static import COMMIT_MESSAGE, ERROR_MESSAGE


def print_info_message(message):
    print('Info   | ' + message)


def print_commit_message():
    print('Commit | ' + COMMIT_MESSAGE)
    return COMMIT_MESSAGE


def print_push_error_message():
    print('Error  | ' + ERROR_MESSAGE)


def print_custom_error_message(message):
    print('Error  | ' + message)
