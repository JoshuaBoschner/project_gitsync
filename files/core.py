import logging

from files.executor import git_add, git_commit, git_pull, git_push
from files.helpers import get_directory, get_repository
from files.log import print_info_message

logging.basicConfig(level=logging.INFO)


def git_sync():
    path_to_push = get_directory() + '\\.git'
    print_info_message('Directory to push: ' + path_to_push)

    repo = get_repository(path_to_push)
    print_info_message('Active branch: ' + repo.active_branch.name)

    git_add(repo)
    git_commit(repo)
    git_pull(repo)
    git_push(repo)
