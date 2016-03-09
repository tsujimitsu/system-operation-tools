# -*- coding: utf-8 -*-

import sys
import chardet

def detect_code(words):
  dict = {
    "ascii": u"ASCII",
    "utf-8": u"UTF-8(BOMなし)",
    "UTF-8-SIG": u"UTF-8(BOMあり)",
    "SHIFT_JIS": u"SHIFT_JIS",
    "EUC-JP": u"EUC-JP"
  }
  
  code = chardet.detect(words)['encoding']
  result = ''
  if code in dict:
    result = dict[code]
  else:
    result = 'unknown: ' + code
      
  return result  


def detect_newline(words):
  result = ''
  
  if '\r\n' in words:
    result = 'CRLF'
  elif '\r' in words:
    result = 'CR'
  elif '\n' in words:
    result = 'LF'
  else:
    result = 'unknown'
  
  return result

  
if __name__ == "__main__":
  argc = len(sys.argv)
  if (argc != 2):
    print(u'ファイル名を引数に指定してください。')
    sys.exit(1)
  
  try:
    f = open(sys.argv[1],'rb')
    
  except Exception,e:
    print(e)
    sys.exit(1)
  
  words = f.read()
  print(u'文字コード：' + detect_code(words))
  print(u'改行コード：' + detect_newline(words))
    

# reference
# http://qiita.com/morinokami/items/b6edc3b9cf31f4b8b7d1
# http://inaz2.hatenablog.com/entry/2014/11/07/210545

# install
# pip install chardet