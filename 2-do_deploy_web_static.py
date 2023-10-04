#!/usr/bin/python3
"""Archive Deploy Script"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['3.85.136.177', '54.172.251.28']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    """
    if not os.path.exists(archive_path):
        return False
    
    try:
        # Upload the archive to the /tmp/ directory on the web server
        archive_filename = os.path.basename(archive_path)
        put(archive_path, '/tmp/{}'.format(archive_filename))

        # Create the directory to uncompress the archive
        archive_folder = '/data/web_static/releases/{}'.format(
            archive_filename.split('.')[0]
        )
        run('sudo mkdir -p {}'.format(archive_folder))

        # Uncompress the archive into the folder
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_filename, archive_folder))

        # Delete the uploaded archive
        run('sudo rm /tmp/{}'.format(archive_filename))

        # Move the contents to the proper location
        run('sudo mv {}/web_static/* {}'.format(archive_folder, archive_folder))

        # Remove the empty web_static folder
        run('sudo rm -rf {}/web_static'.format(archive_folder))

        # Delete the old symbolic link and create a new one
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(archive_folder))

        print("New version deployed!")

        return True
    except Exception as err:
        return False
