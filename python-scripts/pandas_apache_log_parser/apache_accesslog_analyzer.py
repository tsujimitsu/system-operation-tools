# -*- coding: utf-8 -*-
#
# comment
#
# reference
# http://symfoware.blog68.fc2.com/blog-entry-1422.html
# http://www.markhneedham.com/blog/2013/10/30/pandas-adding-a-column-to-a-dataframe-based-on-another-dataframe/
# http://jbclub.xii.jp/?p=487
# http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.resample.html
# https://www.quora.com/Are-there-any-free-large-datasets-in-the-format-of-an-Apache-access-log
# http://ita.ee.lbl.gov/html/traces.html
#
# TODO:
# 何を知りたいか
# ・どのパスが一番アクセスされるか
# ・時間帯別アクセス数
# ・時間帯別パスのアクセス数
# ・リファラのアクセス数ランキング
# ・ブラウザランキング
# ・OSランキング
# ・リクエストバイト数別アクセスパスランキング
# ・ステータスの発生頻度（400台、500台の発生がどれぐらいか）

import apache_log_parser
import pandas as pd
import numpy as np


# debug
from pprint import pprint


if __name__ == '__main__':
    sample = '127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I ;Nav)"'
    parser = apache_log_parser.make_parser('%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"')

    log_data = parser(sample)
    
    df = pd.DataFrame(columns=['datetime','requestpath','referer'])
    
    
    df = df.append(pd.DataFrame([dict(datetime=1,requestpath="a",referer="b")]), ignore_index=True)

    df = df.append(pd.DataFrame([dict(datetime=1,requestpath="a",referer="b")]), ignore_index=True)
    df = df.append(pd.DataFrame([dict(datetime=1,requestpath="a",referer="b")]), ignore_index=True)
    df = df.append(pd.DataFrame([dict(datetime=1,requestpath="a",referer="b")]), ignore_index=True)
    
    df = df.append(pd.DataFrame([dict(datetime=log_data['time_received_datetimeobj'],requestpath=log_data['request_url'],referer=log_data['request_header_referer'])]), ignore_index=True)
    
    print df
    
    
    if 0: #0 print, 1 exit
        exit()

    #pprint(log_data)
    
    # datetime
    print log_data['time_received_datetimeobj']
    
    # status
    print log_data['status']
   
    # request path
    print log_data['request_url']
    
    # referer
    print log_data['request_header_referer']
    
    # browser
    print log_data['request_header_user_agent__browser__family']
    
    # OS
    print log_data['request_header_user_agent__os__family']
    
    # request byte
    print log_data['response_bytes_clf']


