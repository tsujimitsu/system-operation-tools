linux audit
===============

lastlog
---------

* problem

```shell
# lastlog
/var/log/lastlog: No such file or directory
```

* solution

```shell
# touch /var/log/lastlog
# chgrp utmp /var/log/lastlog
# chmod 664 /var/log/lastlog
```


* problem
```shell
# lastlog
root                                       **Never logged in**
```

* solution
```shell
# vim /etc/pam.d/su
session   optional   pam_lastlog.so  nowtmp
```


* reference

1. [Users logging into the server with ssh are not recorded in lastlog](https://www.novell.com/support/kb/doc.php?id=7014881)


sshd
------

* exercises
- restrict ssh login only one user based on user source ip address.

* solution

```shell

Match Address *,!192.168.1.0/27,!192.168.2.0/27 User hogehoge
  PasswordAuthentication no
  PubkeyAuthentication no

```
