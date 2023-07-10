#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime
from os.path import exists


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')

    archive_name = 'web_static_{}.tgz'.format(timestamp)
    archive_path = 'versions/{}'.format(archive_name)

    # Create the versions folder if it doesn't exist
    local('mkdir -p versions')

    # Create the archive
    result = local('tar -czvf {} web_static'.format(archive_path))

    if exists(archive_path):
        return archive_path
    else:
        return None


