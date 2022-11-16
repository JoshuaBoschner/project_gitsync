import os

from git import Repo

from files.log import print_custom_error_message


def get_directory():
    current_working_directory = os.getcwd()
    return current_working_directory


def get_repository(path_to_push):
    try:
        repo = Repo(path_to_push)
    except:
        print_custom_error_message('Failed to find Repository in current directory')
        raise

    return repo
