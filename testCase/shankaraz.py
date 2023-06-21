import requests

from common.get_tlj_auth import *
import qrcode
from PIL import ImageFont, ImageDraw, Image

razlist=[]



def shankaTest(id):

    # id = input("请输入闪卡，数字0-399：")

    id =id
    dataa=razlist[int(id)]
    idd=dataa[0]
    wordd=dataa[1]
    levell=dataa[2]
    data = {"level": levell, "version_code": 20230601, "word": wordd, "word_id": idd, "uid": 1607331624148455426}
    qrdata={"cardType":1,"cardInfo":{"level":levell,"versionCode":20230601,"word":wordd,"wordId":idd}}
    qr = qrcode.QRCode(version=2,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       )
    qr.add_data(qrdata)
    qr.make(fit=True)
    Img=qr.make_image()
    # print(Img)
    savepath=r'C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\shankaraz'

    Img.save(savepath+r"\闪卡第%d张%s.png" %(id,wordd))


    img = Image.open(savepath+r"\闪卡第"+str(id)+"张"+wordd+".png")
    print(img.size)
    draw = ImageDraw.Draw(img)
    # print(draw)
    ttfront = ImageFont.truetype('msyh.ttc', 40,0)  # 字体文件msyh.ttc，需要查找下载
    content = wordd
    width_w, height_h = ttfront.getsize(content)

    # # font = ImageFont.truetype ('arial.ttf', font_size)
    # ascent, descent = ttfront.getmetrics ()
    # (width, baseline), (offset_x, offset_y) = ttfront.getsize(content)
    # print((width, baseline), (offset_x, offset_y))

    print(content)
    draw.text(((650-width_w)/2, 600), content, font=ttfront)  # 文字位置，正文内容，文字RGB颜色，字体
    img.save(r"C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\闪卡图片\闪卡第"+str(id)+"张"+wordd+".png")

    req=requests.post(url=url,json=data,headers=header)
    print(req.json())
