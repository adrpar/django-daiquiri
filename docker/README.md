First build docker containes by running

sh ./build_docker.sh



How to start all this (STILL NOT WORKING)

cd mariadb
docker build -t daiquiri_mariadb -f Dockerfile .
export MYSQL_ROOT_PASSWORD='password'

docker network create daiquiri_network --driver bridge

docker run -p 3306:3306 --name daiquiri_mariadb -v /Users/adrian/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD --net daiquiri_network -d daiquiri_mariadb

If things work:

docker run --name daiquiri --net daiquiri_network daiquiri 


But since things don't work:

For shell access to fix stuff:

docker run -ti -p 8000:8000 --net daiquiri_network daiquiri /bin/bash




