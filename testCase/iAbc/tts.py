import pyttsx3

# 初始化tts引擎
engine = pyttsx3.init()

# 设置要转换的文本
text = "Hello, how are you?"

# 转换文本为语音
engine.say(text)

# 播放语音
engine.runAndWait()

