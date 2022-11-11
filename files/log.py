from conf.static import COMMIT_MESSAGE, ERROR_MESSAGE, INFO_GIT, INFO_GIT_COMMIT, INFO_GIT_ERROR


def print_info_message(message):
    print(INFO_GIT + message)


def print_commit_message():
    print(INFO_GIT_COMMIT + COMMIT_MESSAGE)
    return COMMIT_MESSAGE


def print_push_error_message():
    print(INFO_GIT_ERROR + ERROR_MESSAGE)


def print_custom_error_message(message):
    print(INFO_GIT_ERROR + message)
