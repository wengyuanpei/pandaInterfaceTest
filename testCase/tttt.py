import qrcode



def qrTest():
    qrdata ={"/"}
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4
    )
    qr.add_data(qrdata)
    qr.make(fit=True)
    Img = qr.make_image()
    Img.save(r"C:\Users\zhang\Desktop\管控图片.png")
    print('测试图片生成成功！！')

def lennn():
    print(len('URI="https://videoenc.speiyou.com/video/jyy/decrypt?cipherText=8xmX_0ywzvWXkAzuEK1rEam_g1k7B0Ksx8_LdI0ubro=",IV=0x00000000000000000000000000000000'))

if __name__ == '__main__':
    lennn()
    print(131+146)