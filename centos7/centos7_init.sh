#!/bin/bash
# CentOS 7 Initialize setting

HOST_NAME=XXXX
HOST_ADDRESS=XXXX
DNS1=8.8.8.8
DNS2=8.8.4.4

# ==========================================

# Manual Setting
#vi /etc/sysconfig/network-scripts/ifcfg-enoXXXX
#BOOTPROTO=static
#ONBOOT=yes
#IPADDR=XXX.XXX.XXX.XXX
#PREFIX=24
#GATEWAY=XXX.XXX.XXX.XXX
#DNS1=8.8.8.8
#PEERDNS=no
#NM_CONTROLLED=n

#systemctl restart network
#git clone 

# ==========================================

# Hostname
hostnamectl set-hostname $HOST_NAME
echo "$HOST_ADDRESS $HOST_NAME" >> /etc/hosts

# Network
echo "nameserver $DNS1" >> /etc/resolv.conf
echo "nameserver $DNS2" >> /etc/resolv.conf
systemctl disable NetworkManager
systemctl stop NetworkManager
systemctl enable network
systemctl start network

# Firewall
systemctl disable firewalld
systemctl stop firewalld
systemctl start iptables
systemctl enable iptables

# SELinux
sed -i.bak "/SELINUX/s/enforcing/permissive/g" /etc/selinux/config
setenforce 0

# Time
timedatectl set-timezone Asia/Tokyo

# Package
yum -y update
yum -y install iptables-services
yum -y install git

