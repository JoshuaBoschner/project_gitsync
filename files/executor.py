from files.log import print_commit_message, print_custom_error_message, print_info_message


def git_push(repo):
    print_info_message('Trying to ')
    try:
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print_custom_error_message('Failed to ')
    finally:
        print_info_message('Successfully ')


def git_add(repo):
    print_info_message('Trying to add changes from working directory to staging area')
    try:
        repo.git.add(all=True)
    except:
        print_custom_error_message('Failed to add changes from working directory to staging area')
    finally:
        print_info_message('Successfully added changes from working directory to staging area')


def git_commit(repo):
    print_info_message('Trying to ')
    try:
        repo.index.commit(print_commit_message())
    except:
        print_custom_error_message('Failed to ')
    finally:
        print_info_message('Successfully ')


def git_pull(repo):
    print_info_message('Trying to ')
    try:
        repo.git.pull()
    except:
        print_custom_error_message('Failed to ')
    finally:
        print_info_message('Successfully ')
