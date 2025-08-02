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