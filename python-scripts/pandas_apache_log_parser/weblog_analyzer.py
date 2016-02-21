# -*- coding: utf-8 -*-

#
# comment
#

from collections import Counter


ipaddress_list = []
method_list = []
requested_list = []
referal_list = []
mylist = []


data = open('access.log').readlines()
for line in data:
    ipaddress_list.append(line.split()[0])
    requested_list.append(line.split()[6])
    mylist.append(line.split()[2])

count_ip = Counter(ipaddress_list)
count_requested = Counter(requested_list)


#print count_ip.most_common()
#print count_requested.most_common()
print mylist
