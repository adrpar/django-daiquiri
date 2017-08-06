export DAIQUIRI_PATH=`pwd`

cd docker/mariadb
docker build -t daiquiri_mariadb -f Dockerfile .

cd $DAIQUIRI_PATH
mkdir docker/daiquiri/tmp
cp -r testing docker/daiquiri/tmp/testing
cp -r daiquiri docker/daiquiri/tmp/daiquiri
cp * docker/daiquiri/tmp/.
cd docker/daiquiri
docker build -t daiquiri -f Dockerfile . 
cd $DAIQUIRI_PATH
rm -r docker/daiquiri/tmp
