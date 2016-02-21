# -*- coding: utf-8 -*-

import sys


def chk_num_of_columns(line, correct):
  if len(line) != correct:
    print len(line)
    print('Error: num of columns')

    
def chk_contain_values(value, correct):
  if value in correct:
    pass
  else:
    print('Error: invalid value, ' + value)

    
def chk_not_empty(value):
  if not value:
    print('Error: empty column,' + value)
    
    
def chkfile(words, newline):
  lines = words.split(newline)
  for line in lines:
    
    columns = line.split(',')
    chk_num_of_columns(columns, 4)
    chk_contain_values(columns[0].decode('shift-jis'), ['this',u'これは',1])
    chk_not_empty(columns[1].decode('shift-jis'))

    
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
  chkfile(words, '\r\n')
  
# reference