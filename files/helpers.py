import datetime
import os

from git import Repo


def get_directory():
    current_working_directory = os.getcwd()
    return current_working_directory


def get_repository(path_to_push):
    repo = Repo(path_to_push)
    return repo


def get_current_date():
    return datetime.datetime.now()
