#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""
from fabric.api import env, run, local


env.hosts = ['3.85.136.177', '54.172.251.28']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """
    Deletes out-of-date archives
    keeping the specified number of most recent ones.
    """
    try:
        # Convert number to an integer
        number = int(number)

        if number < 1:
            number = 1

        # Get a list of all archives in the versions folder
        archives_local = local('ls -1t versions', capture=True).split('\n')

        # Delete old archives in the versions folder
        for archive in archives_local[number:]:
            local('rm -f versions/{}'.format(archive))

        # Get a list of all archives in the remote /data/web_static/releases
        archives_remote = run('ls -1t /data/web_static/releases').split('\n')

        # Delete old archives in the remote releases folder on both servers
        for archive in archives_remote[number:]:
            run('rm -f /data/web_static/releases/{}'.format(archive))
        return True
    except Exception:
        return False
