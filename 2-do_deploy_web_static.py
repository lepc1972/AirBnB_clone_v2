#!/usr/bin/python3
""" scripts that distributes a file to web 01 n 02 servers """
import os
from fabric.api import *
from datetime import datetime

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
        put a file in our servers
    """
    if not os.path.exists(archive_path):
        return False
    saved_file = archive_path[9:]
    nv = "/data/web_static/releases/" + saved_file[:-4]
    saved_file = "/tmp/" + saved_file
    put(archive_path, "/tmp/")
    run("sudo mkdir -p {}".format(nv))
    run("sudo tar -xzf {} -C {}/".format(saved_file,
                                         nv))
    run("sudo rm {}".format(saved_file))
    run("sudo mv {}/web_static/* {}".format(nv,
                                            nv))
    run("sudo rm -rf {}/web_static".format(nv))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(nv))

    print("New version deployed!")
    return True
