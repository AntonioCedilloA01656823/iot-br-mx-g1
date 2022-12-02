# Useful Docker Commands
## To spin up MySQL Instance
```
docker run -p 13306:3306 --name mysql-docker-local -e MYSQL_ROOT_PASSWORD=iotbrmx1 -d mysql:latest
```

## To connect to this MySQL Instance
Password: MYSQL_ROOT_PASSWORD
```
mysql --host=127.0.0.1 --port=13306 -u root -p
```
## MySQL shell:
```
CREATE DATABASE eq1Events;
USE eq1Events;
exit
```

## Run Python Scripts

### Create virtual Environment

```
python -m venv myenv
source myenv/bin/activate
pip install -r ./requirements.txt
```

Your terminal should look like the following text:
(myenv) rafael@rafael:~/Desktop/ITA/CES-35/iot-br-mx-g1/STEP3$

### Run

```
python publish.py
python subscribe.py
``

# VIDEO LINK