# Setup Mosquitto

## Install mosquitto
Follow the steps on this link: https://www.vultr.com/docs/install-mosquitto-mqtt-broker-on-ubuntu-20-04-server/

## Config mosquitto files
Copy the content on mqtt_basic to the /etc/mosquitto:

```
sudo cp ./mqtt_basic/central_mosquitto.conf /etc/mosquitto
sudo cp ./mqtt_basic/local_mosquitto.conf /etc/mosquitto
sudo cp ./mqtt_basic/password /etc/mosquitto
```

Check if content is correct:
```
cat /etc/mosquitto/central_mosquitto.conf
cat /etc/mosquitto/local_mosquitto.conf
cat /etc/mosquitto/password
```

Give read permissions to password:

```
sudo chmod +r /etc/mosquitto/password
```

## Run Python Scripts

### Create virtual Environment

```
python -m venv myenv
source myenv/bin/activate
```

Your terminal should look like the following text:
(myenv) rafael@rafael:~/Desktop/ITA/CES-35/iot-br-mx-g1/STEP2$

### Run Mosquitto

```
sudo mosquitto -c /etc/mosquitto/central_mosquitto.conf -v
sudo mosquitto -c /etc/mosquitto/local_mosquitto.conf -v
```