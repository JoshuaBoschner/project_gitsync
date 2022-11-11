from files.log import print_commit_message, print_custom_error_message, print_info_message


def git_push(repo):
    print_info_message('Trying to push changes to remote repository')
    try:
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print_custom_error_message('Failed to push changes to remote repository')
        raise
    finally:
        print_info_message('Successfully push changes to remote repository')


def git_add(repo):
    print_info_message('Trying to add changes from working directory to staging area')
    try:
        repo.git.add(all=True)
    except:
        print_custom_error_message('Failed to add changes from working directory to staging area')
        raise
    finally:
        print_info_message('Successfully added changes from working directory to staging area')


def git_commit(repo):
    print_info_message('Trying to commit staged changes to local repository')
    try:
        commit_message = print_commit_message()
        repo.index.commit(commit_message)
    except:
        print_custom_error_message('Failed to commit staged changes to local repository')
        raise
    finally:
        print_info_message('Successfully committed staged changes to local repository')


def git_pull(repo):
    print_info_message('Trying to pull changes from remote repository')
    try:
        repo.git.pull()
    except:
        print_custom_error_message('Failed to pull changes from remote repository')
        raise
    finally:
        print_info_message('Successfully pulled changes from remote repository')
