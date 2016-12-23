#!/bin/bash
# RHEL7 Create local yum repository

mount /dev/cdrom /mnt
mkdir -p /opt/local-repo/rhel-media
cp -Rp /mnt/* /opt/local-repo/rhel-media
cd /; umount /mnt

rpm -ivh /opt/local-repo/rhel-media/Packages/deltarpm-*.x86_64.rpm
rpm -ivh /opt/local-repo/rhel-media/Packages/python-deltarpm-*.x86_64.rpm
rpm -ivh /opt/local-repo/rhel-media/Packages/createrepo-*.noarch.rpm

createrepo -g /opt/local-repo/rhel-media/repodata/*-comps-Server.x86_64.xml /opt/local-repo/rhel-media/Packages/

cat << EOT > /etc/yum.repos.d/local-repo.repo
[rhel-media]
name=rhel-media
baseurl=file:///opt/local-repo/rhel-media/Packages/
enabled=1
gpgcheck=0
EOT

yum clean all
yum repolist
yum grouplist