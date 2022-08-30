import random
import paho.mqtt.client as mqtt

broker_url = 'emqx-dev.xiongmaoboshi.com'
port = 1883
client_id = str(random.randint(0, 1000))+'test'
HOST = broker_url
PORT =port

def on_connect(client, userdata, flags, rc):
    print("Connected with result code :0 表示连接成功  其它表示失败" + str(rc))
    client.subscribe("chanel_01")


def main():
    client = mqtt.Client(client_id)
    client.connect(HOST, PORT, 60)
    client.on_connect = on_connect
    client.username_pw_set(client_id,password='token')
    client.loop_forever()


if __name__ == '__main__':
    main()







