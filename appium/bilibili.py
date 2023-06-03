from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
    'platformName':'Android',
    'platformVersion':'7.1.2',
    'deviceName':'SM_G955N',
    'appPackage':'tv.danmaku.bili',
    'appActivity':'.MainActivityV2',
    'unicodeKeyboard':True,
    'resetKeyboard':True,
    'newCommandTimeout':10000,
    'automationName':'UiAutomator2',
    #'app':r'd:\apk\bili.apk',
}

#连接appium server,初始化自动化环境
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
iknow=driver.find_element(By.ID,'agree')
#xknow=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView")
if iknow:
    iknow.click()
# elif xknow:
#     xknow.click()
# driver.find_element(By.ID,'expand_search').click()
# driver.find_element(By.ID,'search_src_text').send_keys('白月黑羽')
# driver.press_keycode(AndroidKey.ENTER)
driver.find_element(By.XPATH,"//*[@resource-id='tv.danmaku.bili:id/tabs']//android.view.ViewGroup[3]").click()
tx=driver.find_element(By.XPATH,"//android.view.ViewGroup[5]/android.widget.TextView").text
print(tx)
input("提示:按Enter键结束")
driver.quit()