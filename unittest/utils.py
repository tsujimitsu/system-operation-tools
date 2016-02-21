# -*- coding: utf-8 -*-
# utils.py

def calc(data):
    if isinstance(data, (int, long)): 
        return data * 10
    else:
        raise TypeError('Must supply number', 'found: %r' % data)

