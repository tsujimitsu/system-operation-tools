#!/bin/bash
# RHEL7 Create local yum repository

# Use RHN Online Repository
RH_USERNAME=XXX
RH_PASSWORD=XXX


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

exit 0


# Redhat Network
subscription-manager register --username $RH_USERNAME --password $RH_PASSWORD
subscription-manager subscribe --auto
subscription-manager repos --list-enabled

#REPONAME=rhel-ha-for-rhel-7-server-eus-rpms
#mkdir -p /opt/local-repo/$REPONAME/Packages
#reposync -r $REPONAME -p /opt/local-repo/$REPONAME/Packages/

yum -y install yum-utils

# RHEL7
repolist="rhel-ha-for-rhel-7-server-eus-rpms rhel-7-server-eus-rpms rhel-7-server-rpms rhel-ha-for-rhel-7-server-rpms"
for repo in $repolist; do
    reposync -r $repo -p /opt/local-repo/
done

# OpenStack
repolist="rhel-7-server-openstack-10-tools-rpms rhel-7-server-openstack-9-tools-rpms rhel-7-server-openstack-8-tools-rpms rhel-7-server-openstack-7.0-tools-rpms "
for repo in $repolist; do
    reposync -r $repo -p /opt/local-repo/
done
