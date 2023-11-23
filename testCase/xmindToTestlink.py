


'''

xmind 格式转xmind
文件打包命令 -i 使用图标
Pyinstaller -F -i C:\Users\zhang\Desktop\捕获.PNG  xmindToTestlink.py

'''
import os


path=input("请输入文件的绝对路径如 C:data/a.xmind : " )
if path=='':
    print('未输入内容！请重新输入')
    path = input("请输入文件的绝对路径如：C:data/a.xmind")
print('文件路径',path)
commond='xmind2testlink '+path
os.system(commond)


