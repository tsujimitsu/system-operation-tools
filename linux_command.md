Linux Command
===============

lastlog
---------

* problem

    # lastlog
    /var/log/lastlog: No such file or directory

* solution

    # touch /var/log/lastlog
    # chgrp utmp /var/log/lastlog
    # chmod 664 /var/log/lastlog

* reference
[Users logging into the server with ssh are not recorded in lastlog](https://www.novell.com/support/kb/doc.php?id=7014881)