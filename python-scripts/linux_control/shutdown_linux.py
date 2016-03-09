# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from subprocess import PIPE, Popen
import syslog
import os

def cmdline(command):
    """
    Run linux command
    :param command: str
    :return: Popen
    """
    return Popen(
        args=command,
        stdout=PIPE,
        stderr=PIPE,
        shell=True
    )


if __name__ == '__main__':
    prefix = 'cd / && {}'

    cmd1 = 'who | wc -l'
    p1 = cmdline(prefix.format(cmd1))
    stdout_data, stderr_data = p1.communicate()
    out1 = int(stdout_data.split('\n')[0])

    if out1 == 0:
        syslog.syslog("none login user. shutdown server")
        cmd2 = '/sbin/shutdown -h now'
        p2 = cmdline(cmd2)
        stdout_data, stderr_data = p2.communicate()

    else:
        syslog.syslog("now exist login user. suspend os shutdown.")
