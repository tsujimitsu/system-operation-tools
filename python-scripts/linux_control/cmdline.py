# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from subprocess import PIPE, Popen


def cmdline(prefix, command):
    """
    Run Linux command
    :param command: str
    :return: Popen
    """
    return Popen(
        args=prefix.format(command),
        stdout=PIPE,
        stderr=PIPE,
        shell=True
    )


if __name__ == '__main__':
    print 1
    # prefix = 'cd / && {}'
    # cmd1 = 'who | wc -l'
    # p1 = cmdline(prefix, cmd1)
    # out, err = p1.communicate()
    # print(out.decode('utf-8'))



# reference
# [LinuxコマンドをPythonから上手に扱う方法](http://qiita.com/haminiku/items/7c3f9b83cc6e8dc13027)
# [Pythonのsubprocessで標準出力をリアルタイムに取得する](http://qiita.com/megmogmog1965/items/5f95b35539ed6b3cfa17)
