#河北教育教师网远程培训自动答题下一节功能
#python 3.8
#selenium 4.1.2
#pyautoGUI 0.9.53(取对话框部分)

from selenium import webdriver
from time import sleep
import pyautogui
from selenium.webdriver.common.by import By
import sys

#实例化Chrome浏览器
try:
    hb=webdriver.Chrome()
    hb.get('https://www.hbte.com.cn/')#获取网址
    #弹出确认对话框
    # pyautogui.alert(title='提醒',text='欢迎测试!交流学习\n QQ群:622546750\n')
except:
    #浏览器异常将退出python
    pyautogui.alert(title='提醒', text='未检测到Chrome浏览器,请安装Chrome浏览器或升级到最新版.或QQ群:622546750下载其他浏览器版本\n')
    # 退出python
    sys.exit(0)

#获取网页点位并点击后退出循环
while True:
    #一直等到网页加载出对应元素再点击
    try:
        hb.find_element(By.ID,'end_login').click()
        break
    except:#未找到休息1秒
        sleep(1)
key1=hb.find_element(By.XPATH,'//*[@id="form1"]/div/ul/li[1]/input')
key1.send_keys('132521197009150091')
key2=hb.find_element(By.XPATH,'//*[@id="form1"]/div/ul/li[2]/input')
key2.send_keys('Sw4792322')
hb.find_element(By.XPATH,'//*[@id="form1"]/div/ul/li[3]/input').click()
#同上
while True:
    try:
        hb.find_element(By.TAG_NAME,'i').click()
        break
    except:
        sleep(1)
#同上
hb.find_elements(By.CLASS_NAME,'menu_head')[4].click()#项目培训
sleep(1)
hb.find_elements(By.TAG_NAME,'a')[35].click()#进行中的项目
sleep(1)

# while True:
#     try:
#         hb.find_elements(By.XPATH,'/html/body/div[4]/div[2]/div/div[1]/ul/li[3]/a').click()
#         break
#     except:
#         sleep(1)

while True:
    try:
        hb.find_element(By.ID,'tiao').click()
        break
    except:
        sleep(1)
hb.find_element(By.ID,'like-tk-close').click()
# hb.find_element(By.XPATH,'/html/body/div[3]').click()
#定位到-课程章节页面
while True:
    try:
        if hb.find_element(By.TAG_NAME,'h2').text == '课程章节':
            zhangjie=pyautogui.prompt(title='请输入',text='从本章的第几小节开始学习?请输入\n,取消退出程序',default=1)
            break
    except:
        sleep(1)

n=int(zhangjie)

#定义函数:播放第N小节
def bofang(n):
    div=hb.find_element(By.CLASS_NAME,'courseName_div')
    li_list=div.find_elements(By.TAG_NAME,'a')#小节列表
    li_list[n-1].click()#播放第N小节

#定义函数:点击回答问题,播完后自动进入下一节
def dianjibofang(n):
    while True:
        #点击问题并回答
        try:
            #进入第一层frame
            hb.switch_to.frame(hb.find_element(By.CSS_SELECTOR, '[scrolling="auto"]'))
            #再进入第二层frame并点击
            hb.switch_to.frame(hb.find_element(By.CSS_SELECTOR,'[scrolling="no"]'))
            hb.find_element(By.TAG_NAME,'button').click()
            hb.switch_to.default_content()
            sleep(1)
        except:
            #退出frame回到主页面
            hb.switch_to.default_content()
            sleep(1)

        #自动进入下一节播放部分
        #finally为必须执行,else为无异常时执行
        finally:
            #重新进入第一层frame并查找是否播完
            try:
                #进入frame
                hb.switch_to.frame(hb.find_element(By.CSS_SELECTOR, '[scrolling="auto"]'))
                #查找是否播完
                hb.find_element(By.CSS_SELECTOR, '[style="background: rgb(250, 250, 250); width: 100%;"]')
                #退出frame回到主页
                hb.switch_to.default_content()
                #播放完成,自动加1并播放
                n+=1
                #若未超过总节数_播放
                if n<=len(hb.find_element(By.CLASS_NAME,'courseName_div').find_elements(By.TAG_NAME,'a')):
                    bofang(n)
                #否则本章完成并提示
                else:
                    pyautogui.alert(title='本章完成',text='本章完成!请选择下一课程播放')
                    sleep(4)
                    break
            except:
                #异常时退出frame
                hb.switch_to.default_content()
                sleep(1)

#执行播放,点击,下一节,并重复执行
for e in range(9):
    bofang(n)
    dianjibofang(n)
    while True:
        try:
            if hb.find_element(By.TAG_NAME,'h2').text == '课程章节':
                zhangjie=pyautogui.prompt(title='请输入',text='从本课的第几小节开始学习?请输入',default=1)
                break
        except:
            sleep(1)

    n=int(zhangjie)

pyautogui.alert(title='提醒',text='测试结束\n,获取新测试程序:QQ群:622546750')

#播放下一节,模拟鼠标点击程序
#没有进入frame,无法完成点击,弃用这部分程序
'''
#导入动作
from selenium.webdriver.common.action_chains import ActionChains 
ac=ActionChains(hb)
sleep(5)
#移动到元素
ac.move_to_element(hb.find_element(By.CLASS_NAME,'qplayer-controlswrapper'))
sleep(1)
print(4)
ac.move_to_element(hb.find_element(By.CLASS_NAME,'qplayer-controls'))
sleep(1)
print(5)
ac.move_to_element(hb.find_element(By.CLASS_NAME,'qplayer-barwrapper'))
sleep(1)
print(6)
ac.move_to_element(hb.find_element(By.CLASS_NAME,'qplayer-barcurr'))
sleep(1)
print(7)
'''



