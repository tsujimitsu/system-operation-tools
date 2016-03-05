# -*- coding: utf-8 -*-

import time

class Calc:
    def add(self, x):
        return x * 10


def somefunc():
    print 1


def bettercode():
    
    # file open
    with open("./test.txt") as f:
        for line in f:
            print(line)



if __name__ == '__main__':
    start_time = time.time()
    somefunc()
    elapsed_secs = time.time() - start_time

    print 'elapsed time: %f seconds' % elapsed_secs

