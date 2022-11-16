import datetime

from conf.static import COMMIT_MESSAGE, ERROR_MESSAGE, INFO_GIT, INFO_GIT_ADD, INFO_GIT_COMMIT, INFO_GIT_ERROR, INFO_GIT_PULL


def print_info_message(message):
    print(INFO_GIT + message)


def get_commit_message():
    return COMMIT_MESSAGE + ' - ' + str(get_current_date())


def print_commit_message(message):
    print(INFO_GIT_COMMIT + message)


def print_add_message(message):
    print(INFO_GIT_ADD + message)


def print_pull_message(message):
    print(INFO_GIT_PULL + message)


def print_push_error_message():
    print(INFO_GIT_ERROR + ERROR_MESSAGE)


def print_custom_error_message(message):
    print(INFO_GIT_ERROR + message)


def get_current_date():
    return datetime.datetime.now().strftime("%c")
