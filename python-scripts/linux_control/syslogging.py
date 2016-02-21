# -*- coding: utf-8 -*-
import syslog

syslog.syslog(syslog.LOG_INFO, '[INFO] test messages')
syslog.syslog(syslog.LOG_DEBUG, '[DEBUG] test messages')
syslog.syslog(syslog.LOG_WARNING, '[WARN] test messages')
syslog.syslog(syslog.LOG_ERR, '[ERR] test messages')
