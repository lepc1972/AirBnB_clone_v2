#!/usr/bin/python3
"""
script  of fabric, to distribute a file on our servers
"""

import os
from datetime import datetime
from fabric.api import *

env.hosts = ["35.231.46.212", "54.175.152.17"]
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """
        Distribute our file into servers
    """
    if os.path.exists(archive_path):
        storedfile = archive_path[9:]
        nv = "/data/web_static/releases/" + storedfile[:-4]
        storedfile = "/tmp/" + storedfile
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(nv))
        run("sudo tar -xzf {} -C {}/".format(storedfile,
                                             nv))
        run("sudo rm {}".format(storedfile))
        run("sudo mv {}/web_static/* {}".format(nv,
                                                nv))
        run("sudo rm -rf {}/web_static".format(nv))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(nv))

        print("New version deployed!")
        return True

    return False


def deploy():
    """creates and distributes files in our web 01-02"""
    f_path = do_pack()
    if f_path is None:
        return False
    d_ploy = do_deploy(f_path)
    return do_deploy
