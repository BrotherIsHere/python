from selenium import webdriver
from time import sleep
import pyautogui
from selenium.webdriver.common.by import By
import sys

try:
    hb=webdriver.Chrome()  #或Ie()
    hb.get('https://www.hbte.com.cn/')
    pyautogui.alert(title='提醒',text='欢迎测试!交流学习\n QQ群:622546750\n')
except:
    pyautogui.alert(title='提醒', text='未检测到Chrome浏览器,请安装Chrome浏览器或升级到最新版.或QQ群:622546750下载其他浏览器版本\n')
    sys.exit(0)

while True:
    try:
        hb.find_element(By.ID,'end_login').click()

        break
    except:
        sleep(1)

while True:
    try:
        hb.find_element(By.TAG_NAME,'i').click()

        break
    except:
        sleep(1)

hb.find_elements(By.CLASS_NAME,'menu_head')[4].click()#项目培训


sleep(1)
hb.find_elements(By.TAG_NAME,'a')[35].click()#进行中的项目


sleep(1)

while True:
    try:
        hb.find_elements(By.CLASS_NAME,'jinxingProduct_2')[1].click()

        break
    except:
        sleep(1)

while True:
    try:
        hb.find_element(By.ID,'tiao').click()

        break
    except:
        sleep(1)

while True:
    try:
        hb.find_elements(By.CLASS_NAME,'color-green')[0].click()

        break
    except:
        sleep(0)
#定位到-课程章节页面
while True:
    try:
        if hb.find_element(By.TAG_NAME,'h2').text == '课程章节':
            zhangjie=pyautogui.prompt(title='请输入',text='从本章的第几小节开始学习?请输入\n,取消退出程序',default=1)
            break
    except:
        sleep(1)

n=int(zhangjie)
#播放第N小节
def bofang(n):
    div=hb.find_element(By.CLASS_NAME,'courseName_div')
    li_list=div.find_elements(By.TAG_NAME,'a')#小节列表
    li_list[n-1].click()#播放第N小节




#点击回答问题

def dianjibofang(n):
    while True:

        try:
            hb.switch_to.frame(hb.find_element(By.CSS_SELECTOR, '[scrolling="auto"]'))
            hb.switch_to.frame(hb.find_element(By.CSS_SELECTOR,'[scrolling="no"]'))
            hb.find_element(By.TAG_NAME,'button').click()
            hb.switch_to.default_content()
            sleep(1)
        except:
            hb.switch_to.default_content()
            sleep(1)
        finally:
            try:
                hb.switch_to.frame(hb.find_element(By.CSS_SELECTOR, '[scrolling="auto"]'))
                hb.find_element(By.CSS_SELECTOR, '[style="background: rgb(250, 250, 250); width: 100%;"]')
                hb.switch_to.default_content()
                n+=1
                if n<=len(hb.find_element(By.CLASS_NAME,'courseName_div').find_elements(By.TAG_NAME,'a')):
                    bofang(n)
                else:
                    pyautogui.alert(title='本章完成',text='本章完成!请选择下一课程播放')
                    sleep(4)
                    break
            except:
                hb.switch_to.default_content()
                sleep(1)


for e in range(3):
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


