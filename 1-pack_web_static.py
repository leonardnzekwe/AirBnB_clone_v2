#!/usr/bin/python3
"""Web Static Pack Script"""
from fabric.api import local
from datetime import datetime


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
