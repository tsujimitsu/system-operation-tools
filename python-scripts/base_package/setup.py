#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from setuptools import setup
from setuptools import find_packages

sys.path.append('./hello')
sys.path.append('./test')

def main():
    setup(
        name = 'hello',
        version = '1.0.0',
        description = 'python base package',
        author = 'Toshimitsu Tsuji',
        author_email = 'tsujimitsu@gmail.com',
        packages = find_packages(),
        test_suite = 'test_hello.suite',
    )


if __name__ == '__main__':
    main()
