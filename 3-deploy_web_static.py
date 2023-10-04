#!/usr/bin/python3
"""Archive Deploy Script"""
from fabric.api import env, run, put, local
from datetime import datetime
import os


env.hosts = ['3.85.136.177', '54.172.251.28']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Get the current date and time
    now = datetime.now()

    # Format the archive filename
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )

    # Format the tar command
    tar_command = "tar -cvzf versions/{} web_static".format(archive_name)

    # Compress the web_static folder into a .tgz archive and
    # Use the capture parameter to capture the exit code
    result = local(tar_command, capture=True)

    # Check if the archive was created successfully
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None


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
        run('sudo tar -xzf /tmp/{} -C {}'.format(
            archive_filename, archive_folder
        ))

        # Delete the uploaded archive
        run('sudo rm /tmp/{}'.format(archive_filename))

        # Move the contents to the proper location
        run('sudo mv {}/web_static/* {}'.format(
            archive_folder, archive_folder
        ))

        # Remove the empty web_static folder
        run('sudo rm -rf {}/web_static'.format(archive_folder))

        # Delete the old symbolic link and create a new one
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(archive_folder))

        # All Operations were successful
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    Function to automate the deployment process.
    """
    # Call the do_pack function to create the archive and get its path
    archive_path = do_pack()

    if not archive_path:
        return False

    # Call the do_deploy function with the archive_path on remote servers
    return do_deploy(archive_path)
