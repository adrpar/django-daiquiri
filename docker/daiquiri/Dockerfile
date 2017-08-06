FROM ubuntu:17.10

RUN apt-get update && \
    apt-get install -y git build-essential libxml2-dev libxslt-dev zlib1g-dev libssl-dev python3-dev python3-venv && \
    apt-get install -y software-properties-common && \
	apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8 && \
	add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://mirror.rackspeed.de/mariadb.org/repo/10.1/ubuntu zesty main' && \
	apt-get update && \
	apt-get install -y mariadb-client libmariadbd-dev libmariadbclient-dev

COPY ./tmp /daiquiri

ENV DAIQUIRI_APP "https://github.com/aipescience/django-daiquiri-app"

RUN mkdir /daiquiri/daiquiri/auth/management && \
    mkdir /daiquiri/daiquiri/auth/management/commands && \
    touch /daiquiri/daiquiri/auth/management/__init__.py && \
    touch /daiquiri/daiquiri/auth/management/commands/__init__.py

COPY initadmin.py /daiquiri/daiquiri/auth/management/commands/initadmin.py

RUN cd /daiquiri && \
	git clone $DAIQUIRI_APP /daiquiri_app && \
	cd /daiquiri_app && \
	python3 -m venv /runenv && \
	. /runenv/bin/activate && \
	pip3 install /daiquiri && \
	pip3 install mysqlclient && \
	mkdir log download

COPY daiquiri_app_settings.py /daiquiri_app/config/settings/local.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
CMD [""]





