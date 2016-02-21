# -*- coding: utf-8 -*-

#import pandas as pd
#import numpy as np


#df = pd.read_csv('access.log', header=None, names=['ip', 'identd', 'user', 'datetime', 'method', 'request', 'status', 'size', 'referer', 'agent', 'other'])

#print df

#dfm = df.ip.resample('T', how='count')
#print dfm

import apache_log_parser

sample = '127.0.0.1 111 222 999 888 [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I ;Nav)"'
parser = apache_log_parser.make_parser('%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"')

log_data = parser(sample)
print 'status:' + log_data['status']
print 'remote_logname:' + log_data['remote_logname']
print 'user:' + log_data['remote_user']
