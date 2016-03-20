# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from subprocess import PIPE, Popen
import os
from py2ipaddress import ipaddress as ia

def cmdline(command):
    """
    Run Linux command
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
    cmd1 = "cd / && last | egrep -v 'system boot|^wtmp|^$' | awk '{print $3}' | sort | uniq"
    p1 = cmdline(cmd1)
    out, err = p1.communicate()

    print ia.ip_address(u'192.168.1.31') in ia.ip_network(u'192.168.1.0/27')
    print ia.ip_address(u'192.168.1.32') in ia.ip_network(u'192.168.1.0/27')
    #for ip in out:
    #    print ip
