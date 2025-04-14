import pyttsx3


# 初始化
engine = pyttsx3.init()
# 设置要转换的文本
text = """
从前，有一座美丽的大森林，森林里住着许多小动物，它们每天过着无忧无虑的生活。有一天，森林里来了几个伐木工人
"""
#音量
rate=engine.getProperty('rate')
print(rate)
#语速
volume=engine.getProperty('volume')
print(volume)
#重新定义音量语速
engine.setProperty('rate',150)
engine.setProperty('volume',1.5)
# 播放语音
engine.say(text)
engine.runAndWait()
engine.stop()
#保存音频文件
engine.save_to_file('音频文件！',r'C:\Users\zhang\Desktop\bugreport\12.MP3')
