import random
import requests
from common.get_tlj_auth import *
import qrcode
from PIL import ImageFont, ImageDraw, Image



def shankaTest(disc,num_list,id):

    # id = input("请输入闪卡，数字0-399：")

    qrdata=id
    qr = qrcode.QRCode(version=2,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       )
    qr.add_data(qrdata)
    qr.make(fit=True)
    Img=qr.make_image()
    savepath=r"C:\Users\zhang\Documents\pandaInterfaceTest\testCase\闪卡图片\%s第%d张id为%d.png" %(disc,num_list,id)
    # print(Img)
    Img.save(savepath)


    img = Image.open(savepath)
    print(img.size)
    draw = ImageDraw.Draw(img)
    # print(draw)
    ttfront = ImageFont.truetype('msyh.ttc', 40,0)  # 字体文件msyh.ttc，需要查找下载
    content = str(id)
    width_w, height_h = ttfront.getsize(content)

    # # font = ImageFont.truetype ('arial.ttf', font_size)
    # ascent, descent = ttfront.getmetrics ()
    # (width, baseline), (offset_x, offset_y) = ttfront.getsize(content)
    # print((width, baseline), (offset_x, offset_y))

    print(content)
    draw.text(((330-width_w)/2, 280), content, font=ttfront)  # 文字位置，正文内容，文字RGB颜色，字体
    img.save(savepath)


if __name__ == '__main__':
    razbooklist=[1820,1823]

    disc=str('RAZ正确绘本')

    i=0
    for id in list(razbooklist):
        # id=random.choice(razbooklist)
        shankaTest(disc,i,id)
        i+=1


    randomidlist = [999, 666, 555, 111, 000, 2000014, 1823,1820]

    disc1=('非绘本')
    a = 0
    for idd in list(randomidlist):
        # id=random.choice(razbooklist)
        shankaTest(disc1, a, idd)
        a += 1


