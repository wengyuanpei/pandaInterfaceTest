"""
环境准备：
1、appium 图形化界面工具，使用inspcter进行页面元素获取 、java环境、node.js环境
2、安装Android SDK
3、python appium 本地开发环境  pip install Appium-Python-Client -i https://pypi.tuna.tsinghua.edu.cn/simple
"""



from time import sleep
from xmlrpc.client import Boolean
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {
  "platformName": "Android",
  "appium:deviceName": "94a3ad11",
  "appium:appPackage": "com.minhui.networkcapture",
  "appium:appActivity": "com.minhui.networkcapture.ui.SpalishActivity",
  "appium:automationName": "UiAutomator2",
  "appium:noReset": Boolean(1),
    "browserName": ""
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
sleep(2)
try:

    driver.find_element(AppiumBy.ID, "android:id/button2").click()
    sleep(2)
finally:
    driver.quit()