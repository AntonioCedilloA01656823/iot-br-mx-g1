# Useful Docker Commands
- To spin up MySQL Instance
docker run -p 13306:3306 --name mysql-docker-local -e MYSQL_ROOT_PASSWORD=iotbrmx1 -d mysql:latest
- To connect to this MySQL Instance
mysql --host=127.0.0.1 --port=13306 -u root -p
