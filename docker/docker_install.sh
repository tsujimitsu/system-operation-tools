#!/bin/bash
# docker and docker-compose install on CentOS 7

cat << 'EOF' | sudo tee /etc/yum.repos.d/docker.repo > /dev/null
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/7/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
EOF

sudo yum clean all
sudo yum -y install docker-engine
sudo systemctl start docker
sudo systemctl enable docker

curl -L "https://github.com/docker/compose/releases/download/1.9.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

docker version
docker-compose --version
