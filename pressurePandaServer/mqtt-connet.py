import random
import time

import paho.mqtt.client as mqtt
from pandaInterfaceTest.parameter.getMqttToken import getmqtttoeken



mqttpara=getmqtttoeken()
mqtttoeken=mqttpara[0]
mqttsn=mqttpara[1]


broker_url = 'emqx-dev.xiongmaoboshi.com'
port = 1883
client_id = mqttsn
HOST = broker_url
PORT =port

def on_connect(client, userdata, flags, rc):
    print("Connected with result code :0 表示连接成功  其它表示失败，rc：" + str(rc))
    client.subscribe("chanel_01")


def main():
    client = mqtt.Client(client_id)
    client.connect(HOST, PORT, 60)
    client.on_connect = on_connect
    client.username_pw_set(client_id,password=mqtttoeken)
    client.loop_forever()  #长连接



main()














