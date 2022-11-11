import os

from git import Repo

from files.log import print_info_message


def get_directory():
    current_working_directory = os.getcwd()
    print_info_message('Directory path: ' + current_working_directory)
    return current_working_directory


def get_repository(path_to_push):
    repo = Repo(path_to_push)
    return repo
