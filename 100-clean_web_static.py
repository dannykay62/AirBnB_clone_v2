from fabric.api import env, run, local
from fabric.operations import put
from fabric.context_managers import cd
from datetime import datetime
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual IP addresses of your web servers


def do_clean(number=0):
    """
    Deletes out-of-date archives from versions folder and web servers.
    """
    number = int(number)
    if number < 1:
        number = 1

    with cd('/data/web_static/releases'):
        # Delete unnecessary archives from versions folder
        archives = run('ls -t | grep web_static_').split()
        to_delete = archives[number:]
        for archive in to_delete:
            run('rm -rf {}'.format(archive))

    with cd('/data/web_static/releases'):
        # Delete unnecessary archives from web servers
        releases = run('ls -t | grep web_static_').split()
        to_delete = releases[number:]
        for release in to_delete:
            run('rm -rf {}'.format(release))
