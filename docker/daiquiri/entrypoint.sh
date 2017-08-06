#!/bin/bash

cd /daiquiri_app
source /runenv/bin/activate
./manage.py sqlcreate | mysql -h daiquiri_mariadb -u admin --password=password || true
./manage.py migrate
./manage.py migrate --database=tap
./manage.py initadmin username email password
./manage.py runserver 0.0.0.0:8000
