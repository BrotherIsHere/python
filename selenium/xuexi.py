#utf-8
import time
from selenium import webdriver
from time import sleep
import pyautogui
import sys
from selenium.webdriver.common.by import By


"""定义播放文字、音乐、视频的函数"""
def bofang():
    try:                                                #如果页面出现‘播报’，则是文字新闻，若不是会出现异常
        if xuexi.find_element(By.CLASS_NAME,'voice-lang-switch').text=='播报':    #没有这个元素则异常
            sleep(2)                                   #文字页面停留70秒
            xuexi.close()
    except:
        try:
            if xuexi.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[1]/div[2]/div[2]/button').text=='查看专辑':
                xuexi.find_element(By.XPATH,
                                   '//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[1]/div[2]/button').click()

                stoptime = xuexi.find_element(By.XPATH,
                                              '//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[3]/div[2]/div[3]/div[4]/span[2]').text
                while True:
                    try:
                        if xuexi.find_element(By.XPATH,
                                              '//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[3]/div[2]/div[3]/div[4]/span[1]').text == stoptime:
                            sleep(3)
                            xuexi.close()
                            break
                    except:
                        sleep(0.5)
        except:
            try:
                while True:                                     #循环等待视频结束，结束时视频会出现重新播放按钮'replay-btn'元素
                    try:                                        #没有重新播放按钮'replay-btn'元素时，会出现异常
                        xuexi.find_element(By.CLASS_NAME,'replay-btn')#查找重新播放按钮'replay-btn'元素，没有则出现异常
                        sleep(3)
                        xuexi.close()
                        break                                   #终止循环
                    except:
                        sleep(3)

            except:
                print('无内容播放')

#捕捉错误并提示，浏览器、断网
try:
    xuexi=webdriver.Chrome()                        #实例化chrome浏览器
    xuexi.get('https://pc.xuexi.cn/points/login.html?ref=https%3A%2F%2Fwww.xuexi.cn%2F')#获取登录页面
except:
    pyautogui.alert(title='提醒', text='未检测到Chrome浏览器,请安装Chrome浏览器或升级到最新版.或QQ群:622546750下载浏览器\n')
    sys.exit(0)
pyautogui.alert(title='提醒',text="欢迎测试!交流学习\n QQ群:622546750\n")
pyautogui.scroll(-1500)                             #鼠标向下滚动1500，使登录二维码位于正中

while True:                                         #不断循环2秒，直到出现登录页面
    try:                                            #捕获异常
        if '您好，欢迎您' in xuexi.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/header/div[2]/div[2]/span/span').text:     #查找页面出现‘你好’元素，说明登录成功
            break                                   #终止循环
    except:
        sleep(2)                                    #等待2秒


#直接实例化‘国际’页面，并点击播放对应页面列表今日更新的新闻元素
xuexi.get('https://www.xuexi.cn/xxqg.html?id=cc8b6dc4f4c042e49fc93c279c41dc14')    #直接获取‘国际’页面，并实例化
date=time.strftime('%Y-%m-%d')                          #格式化本地时间格式为：年-月-日 的形式
sleep(5)
#等待5秒，使网页加载完毕，防止找不到页面元素
datelist=[]                                             #建立空列表，等待将页面各元素存入
classlist=xuexi.find_elements(By.CLASS_NAME,'text')     #查找页面所有text元素（列表）
for dd in classlist:                                    #提取列表元素
    if dd.text==date:                                   #如果元素的字符串与本地时间相同则想入到datelist列表中
        datelist.append(dd)                             #追加到列表中
for ddd in datelist:                                    #依次点击各元素
    ddd.click()                                         #网页可能在新标签页面中打开
    handles=xuexi.window_handles                        #获取所有标签页面的句柄
    xuexi.switch_to.window(handles[-1])                 #定位到新打开的页面
    sleep(5)
    bofang()
    xuexi.switch_to.window(handles[-2])

"""播放视听新闻页面的内容："""
#等待页面加载完毕并点击’学习电视台‘
while True:
    try:
        xuexi.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/header/div[2]/div[1]/div[2]/a[2]').click()
        break
    except:
        sleep(2)
#跳转到新打开的标签页
handles=xuexi.window_handles
xuexi.switch_to.window(handles[-1])

#查找页面并点击第一频道元素
while True:
    try:
        xuexi.find_element(By.XPATH,'//*[@id="495f"]/div/div/div/div/div/section/div/div/div/div[1]/div[1]/div/div/span').click()
        break
    except:
        sleep(2)

#跳转到新页面
handles=xuexi.window_handles
xuexi.switch_to.window(handles[-1])
while True:
    try:
        xuexi.find_element(By.XPATH,'//*[@id="1novbsbi47k-5"]/div/div/div/div/div/div/section/div[1]/span[2]').click()
        sleep(5)
        innlist=[]
        innlists = xuexi.find_elements(By.CLASS_NAME, 'text')
        for ii in innlists:
            if ii.text == date:
                innlist.append(ii)
        break
    except:
        sleep(2)
#点击播放前6个视频
st=0
for inn in innlist:
    if st==6:
        break
    else:
        inn.click()
        #跳转到新页面
        handles = xuexi.window_handles
        xuexi.switch_to.window(handles[-1])
        sleep(5)
        bofang()
        st+=1
        xuexi.switch_to.window(handles[-2])

