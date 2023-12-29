

#xmind 格式转xmind
#文件打包命令 -i 使用图标

#Pyinstaller -F -i C:\Users\zhang\Desktop\捕获.PNG  xmindToTestlink.py

import os
import xmind2testlink


pathData=input("请输入文件的绝对路径如 C:data/a.xmind : ")
# patnSave=input("请输入文件的绝对路径如 C:data/a.xmind : ")
print('文件路径',pathData)
commond='xmind2testlink '+pathData
os.system(commond)


