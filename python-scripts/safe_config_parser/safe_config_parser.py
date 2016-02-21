# -*- coding: utf-8 -*-

# http://symfoware.blog68.fc2.com/blog-entry-1589.html
# http://qiita.com/podhmo/items/5a124d6d4f8362738c87

import ConfigParser


default_config = {
    'host': 'localhost',
    'port': '8080',
    'autorun': 'false'
}

config = ConfigParser.SafeConfigParser(default_config)
config.read('config.ini')

print config.get('Section1', 'host')
print config.getint('Section1', 'port')
print config.getboolean('Section1', 'autorun')
print config.get('Section1', 'address')

portnum = config.getint('Section1', 'port') + 1
config.set('Section1', 'port', str(portnum))

with open('config.ini', 'wb') as f:
    config.write(f)
