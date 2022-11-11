import files.log
from files.core import git_sync

if __name__ == '__main__':
    files.log.print_init_message('Starting git sync process ...')
    git_sync()
