#!/usr/bin/python3
""" fabric script to compress """
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        Return the tgz file if was correctly
        gernerated.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(file_path))

    if t_gzip_archive.succeeded:
        return file_path
    else:
        return None
