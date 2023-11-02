#coding:'utf-8'
import random
import subprocess
import sys
import  os

def send_adb(command):
    subprocess.run(['adb']+ command.split())


if __name__ == '__main__':
    listtt=[]
    a=send_adb('shell logcat | grep -E "PK"')
    # print(a)


    aaa=os.popen(r'C:\Users\zhang\Desktop\听力机\pandaInterfaceTest\testCase\tttt.py')
    for iii in aaa:
        print(iii.replace(('\n',"")))
    print('控制台的输出',aaa)


