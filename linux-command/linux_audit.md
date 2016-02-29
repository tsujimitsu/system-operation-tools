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

* exercises: restrict ssh login only one user based on user source ip address.

* solution

```shell

Match Address *,!192.168.1.0/27,!192.168.2.0/27 User hogehoge
  PasswordAuthentication no
  PubkeyAuthentication no

```

* reference

1. [How can the Address condition in a Match conditional block in sshd_config be negated?](http://serverfault.com/questions/408284/how-can-the-address-condition-in-a-match-conditional-block-in-sshd-config-be-neg)
2. [How to restrict everyone except a certain group in SSH?](http://serverfault.com/questions/44707/how-to-restrict-everyone-except-a-certain-group-in-ssh)
3. [Negative matching on multiple ip addresses in SSH](http://www.nightbluefruit.com/blog/2014/05/negative-matching-on-multiple-ip-addresses-in-ssh/)
