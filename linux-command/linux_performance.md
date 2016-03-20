linux performance
==================

```shell

$ uptime
$ dmesg | tail
$ vmstat 1
$ mpstat -P ALL 1
$ pidstat 1
$ iostat -xz 1
$ free -m
$ sar -n DEV 1
$ sar -n TCP,ETCP 1
$ top



```

* [6万ミリ秒でできるLinuxパフォーマンス分析](https://yakst.com/ja/posts/3601)
* [Netflix at Velocity 2015: Linux Performance Tools](http://techblog.netflix.com/2015/08/netflix-at-velocity-2015-linux.html)
* [Linux Performance Tools 2014](http://www.slideshare.net/brendangregg/linux-performance-tools-2014)



ps
---

```shell
ps auxf
```


mem
-----

```shell
free -tm
```
