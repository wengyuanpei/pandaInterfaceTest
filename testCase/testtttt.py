import matplotlib.pyplot as plt # plt 用于显示图片
import psutil
import requests
from PIL import Image

def imgshow(url,picname):

    img1 = Image.open(url)

    #结果展示
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码
    plt.subplot(111)
    plt.imshow(img1)
    plt.title(picname)
    #不显示坐标轴
    plt.axis('off')
    plt.show()
    plt.pause(2)  # 该句显示图片15秒
    plt.ioff()  # 显示完后一定要配合使用plt.ioff()关闭交互模式，否则可能出奇怪的问题

    plt.clf()  # 清空图片
    plt.close()  # 清空窗口


for i in range(5):
    print("第%s张图片" % (i))
    url='https://file.abctime.com/word/img/2023-05-24/count.png'

    aaaaa=requests.get(url)
    c=aaaaa.content
    # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
    #保存路径
    path=r'C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\闪卡图片\p1'

    with open(path, 'wb') as f:
        f.write(c)
        f.close()


    imgshow(path,'p1')