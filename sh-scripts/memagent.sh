#!/bin/sh
vmstat 5 2 | tail -1 | awk '{print $4,$5,$6}'


