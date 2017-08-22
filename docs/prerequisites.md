Install prerequisites
=====================

Centos 6
--------

### Distribution packages

```
yum install -y git gcc gcc-c++ libxml2-devel libxslt-devel
```

### Python

```
# for python2
yum install -y centos-release-scl
yum install -y python27-devel python27-virtualenv
scl enable python27 bash

# for python3
yum install -y python34-devel
```

### MariaDB 10.2

```
# in /etc/yum.repos.d/MariaDB.repo
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.2/centos6-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
```

```
yum install -y MariaDB MariaDB-server MariaDB-devel

service mysql start
chkconfig mysql on

mysql_secure_installation
```

### RabbitMQ

```
# in /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/20/el/6
gpgcheck=1
gpgkey=https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

```
yum install -y epel-release
yum install -y erlang socat

wget https://github.com/rabbitmq/rabbitmq-server/releases/download/rabbitmq_v3_6_11/rabbitmq-server-3.6.11-1.el6.noarch.rpm

rpm -i rabbitmq-server-3.6.11-1.el6.noarch.rpm

service rabbitmq-server start
chkconfig rabbitmq-server on
```

### Redis

```
yum install -y redis

service redis start
chkconfig redis on
```

### Java

```
yum install -y java-1.8.0-openjdk-headless
```

### Node.js and npm

```
curl --silent --location https://rpm.nodesource.com/setup_6.x | sudo bash -

yum install -y nodejs
```


Centos 7.3
----------

### Distribution packages

```
yum install -y git gcc gcc-c++ libxml2-devel libxslt-devel openssl-devel
```

### Python

```
# for python2
yum install -y python-devel python-virtualenv

# for python3
yum install -y python34-devel
```

### MariaDB 10.1

```
# in /etc/yum.repos.d/MariaDB.repo
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.1/centos73-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
```

```
yum install -y MariaDB MariaDB-server MariaDB-devel

systemctl start mariadb
systemctl enable mariadb

mysql_secure_installation
```

### RabbitMQ

```
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/20/el/7
gpgcheck=1
gpgkey=https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

```
yum install -y epel-release
yum install -y erlang socat

wget https://github.com/rabbitmq/rabbitmq-server/releases/download/rabbitmq_v3_6_11/rabbitmq-server-3.6.11-1.el7.noarch.rpm

rpm -i rabbitmq-server-3.6.11-1.el7.noarch.rpm

systemctl start rabbitmq-server
systemctl enable rabbitmq-server
```
### Redis

```
yum install -y redis

systemctl start redis
systemctl enable redis

```

### Java

```
yum install -y java-1.8.0-openjdk-headless
```

### Node.js and npm

```
curl --silent --location https://rpm.nodesource.com/setup_6.x | sudo bash -

yum install -y nodejs
```

debian 8 (jessie)
-----------------

### Distribution packages

```
apt-get install -y git build-essential libxml2-dev libxslt-dev zlib1g-dev libssl-dev
```

### Python

```
# for python2
apt-get install -y python-dev python-virtualenv

# for python3
apt-get install -y python3-dev
```

### MariaDB 10.1

```
apt-get install -y software-properties-common
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://mirror.rackspeed.de/mariadb.org/repo/10.1/debian jessie main'

apt-get update
apt-get install -y mariadb-client mariadb-server libmariadbd-dev libmariadbclient-dev
```

### RabbitMQ

```
apt-get install -y erlang socat

wget https://github.com/rabbitmq/rabbitmq-server/releases/download/rabbitmq_v3_6_11/rabbitmq-server_3.6.11-1_all.deb

dpkg -i rabbitmq-server_3.6.11-1_all.deb

systemctl start rabbitmq-server
systemctl enable rabbitmq-server
```

### Redis

```
apt-get install -y redis-server
```

### Java

```
apt-get install -y openjdk-7-jre-headless
```

### Node.js and npm

debian 9 (strech)
-----------------

### Distribution packages

```
apt-get install -y git build-essential libxml2-dev libxslt-dev zlib1g-dev libssl-dev
```

### Python

```
# for python2
apt-get install -y python-dev python-virtualenv

# for python3
apt-get install -y python3-dev
```

### MariaDB 10.1

```
apt-get install -y mariadb-client mariadb-server libmariadb-dev libmariadbclient-dev
```

### RabbitMQ

```
apt-get install -y rabbitmq-server

systemctl start rabbitmq-server
systemctl enable rabbitmq-server
```

### Redis

```
apt-get install -y redis-server

systemctl start redis-server
systemctl enable redis-server
```

### Java

```
apt-get install -y openjdk-8-jre-headless
```

### Node.js and npm

```
curl -sL https://deb.nodesource.com/setup_6.x | bash -

apt-get install nodejs
```

Ubuntu 14.04 (Trusty Tahr)
--------------------------

### Distribution packages

```
apt-get install -y git build-essential libxml2-dev libxslt-dev zlib1g-dev
```

### Python

```
# for python2
apt-get install -y python-dev python-virtualenv

# for python3
apt-get install -y python3-dev python3-venv
```

### MariaDB 10.1

```
sudo apt-get install software-properties-common
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
sudo add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://mirror.rackspeed.de/mariadb.org/repo/10.1/ubuntu trusty main'

apt-get update
apt-get install -y mariadb-client mariadb-server libmariadbd-dev libmariadbclient-dev
```

### RabbitMQ

```
apt-get install -y erlang-nox socat

wget https://github.com/rabbitmq/rabbitmq-server/releases/download/rabbitmq_v3_6_11/rabbitmq-server_3.6.11-1_all.deb

dpkg -i rabbitmq-server_3.6.11-1_all.deb
```

### Redis

```
apt-get install -y redis-server
```

### Java

```
apt-get install -y openjdk-7-jre-headless
```

### Node.js and npm

```
curl -sL https://deb.nodesource.com/setup_6.x | bash -

apt-get install nodejs
```

Ubuntu 16.04 (Xenial Xerus)
---------------------------

### Distribution packages

```
apt-get install -y git build-essential libxml2-dev libxslt-dev zlib1g-dev libssl-dev
```

### Python

```
# for python2
apt-get install -y python-dev python-virtualenv

# for python3
apt-get install -y python3-dev
```

### MariaDB 10.1

```
apt-get install software-properties-common
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://mirror.rackspeed.de/mariadb.org/repo/10.1/ubuntu xenial main'

apt-get update
apt-get install -y mariadb-client mariadb-server libmariadbd-dev libmariadbclient-dev
```

### RabbitMQ

```
apt-get install -y rabbitmq-server

systemctl start rabbitmq-server
systemctl enable rabbitmq-server
```

### Redis

```
apt-get install -y redis-server
```

### Java

```
apt-get install -y openjdk-8-jre-headless
```

### Node.js and npm

```
curl -sL https://deb.nodesource.com/setup_6.x | bash -

apt-get install nodejs
```

Further reading
---------------

* https://downloads.mariadb.org/mariadb/repositories
* https://www.rabbitmq.com/download.html.
* https://nodejs.org/en/download/package-manager