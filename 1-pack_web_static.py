#!/usr/bin/python3
""".tgz file obtained from web_static dir"""

from datetime import datetime
from fabric.operations import local


def do_pack():
    local("mkdir -p versions")
    r = local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
              capture=True)
    if r.failed:
        return None
    return r
