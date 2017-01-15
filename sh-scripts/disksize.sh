#!/bin/sh

HOME_DIR=/home

function check_disk_files()
{
	for i in `find $1 -maxdepth 1 -type d`; do
		echo `du -sm $i`;
	done
}

if [ "x$1" != "x" ]; then
	check_disk_files $1 | sort -nr | awk '{printf("%sMB\t%s\n", $1, $2);}';
else
	check_disk_files $HOME_DIR | sort -nr | awk '{printf("%sMB\t%s\n", $1, $2);}';
fi
