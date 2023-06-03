import pyautogui
import time


'''
#获取鼠标当前的位置
h=pyautogui.position()
print(h)

#获取屏幕分辨率
x=pyautogui.size()
print(x)
#当前位置是否在屏幕上
o=pyautogui.onScreen(333,1555)
print(o)
#移动鼠标到某个位置
pyautogui.moveTo(333,100,duration=5)#持续5秒
#从当前位置移动鼠标
pyautogui.move(155,100,duration=2)
dangq=pyautogui.position()# 获取鼠标当前位置
print(dangq)
#拖动鼠标
pyautogui.dragTo(300,300,button='left',duration=5)
pyautogui.drag(-100,200,button='right',duration=5)
'''
#获取鼠标位置
weiz=pyautogui.position()
print(weiz)
'''#移动到我的电脑
#pyautogui.moveTo(51,58)
#双击计算机打开
pyautogui.doubleClick(51,58)
#移动到C盘上
pyautogui.click(436,291)
#右键选属性
pyautogui.click(436,291,button='right')
#pyautogui.moveTo(505,680)
pyautogui.click(525,680)
'''
'''pyautogui.click(98,97,clicks=2)
pyautogui.mouseDown(81,226,duration=2)
pyautogui.mouseUp(188,226,duration=2)'''

'''#pyautogui.scroll(300)
pyautogui.doubleClick(70,109)
pyautogui.write('skdkdkdkdkdkdk',interval=0.5)
pyautogui.press('enter')
pyautogui.write('dkAAAAkkkkk')
pyautogui.press('2',presses=5)
pyautogui.press('enter')
pyautogui.press(['s','w','enter','k'])
pyautogui.press('delete')
pyautogui.hotkey('alt','e')
'''
#20,19;73,65
#pyautogui.screenshot('b.png',[15,15,60,55])
'''l=pyautogui.locateOnScreen('b.png')
l1=pyautogui.locateCenterOnScreen('b.png')
print(l)
print(l1)
pyautogui.doubleClick(l1)'''
'''
#桌面壁纸更换
for i in range(9):
    time.sleep(5)
    pyautogui.rightClick(229,146)
    pyautogui.press('n')'''
'''#警告框
a=pyautogui.alert(text='5秒后开始',button='ok',title='警告')
if a=='ok':
    print(666)
else:
    print(777)
print(a)'''
'''#确认框
b=pyautogui.confirm(text='确认执行?',title='消息',buttons=['确认','取消','不确定'])
print(b)
#消息提示框
c=pyautogui.prompt(title='提示',text='输入信息',default='你的姓名')
print(c)'''
'''d=pyautogui.password(title='密码框',text='请输入密码',default='2222',mask='$')
print(d)
'''
time.sleep(5)
pyautogui.screenshot('b.png',(99,404,30,25))
'''
#166.323,212,361
#查找定位图片位置
a,b =pyautogui.locateCenterOnScreen('1.png')
pyautogui.doubleClick(a+100,b+100)
#212,385,757,693
pyautogui.screenshot('end.png',[168,337,260,60])

#229,889,402,389
pyautogui.screenshot('kechengzj.png',[367,578,90,26])
#播放下一课
#475.504.150,379

#pyautogui.screenshot('end.png',[478,538,180,30])
#定位到'课程章节'


 #在循环最外层
#time.sleep(2)

def xiaojie(n):
    #自动播放第n小节课
    try:
        dd = pyautogui.locateCenterOnScreen('end.png', confidence=0.7)
        pyautogui.doubleClick(dd)
        pyautogui.scroll(-700)
        time.sleep(1)
        kx,ky=pyautogui.locateCenterOnScreen('kechengzj.png')
        kx2,ky2=kx-300,ky+45+50*(n-1)
        pyautogui.doubleClick(kx2,ky2)
        time.sleep(1)
        pyautogui.scroll(-600)
    except:
        pyautogui.alert(title='????', text='视频窗口位置异常?,调整到中央')
        time.sleep(10)


#else:
    #xiaojie(n)
def dianji():
    #自动答题,鼠标在一定范围内点击
    w1,h1=pyautogui.locateCenterOnScreen('1.png')
    h1+=40
    for hj in range(15):
        h2=h1+20*hj
        for wj in range(10):
            w2=w1+20*wj
            pyautogui.click(w2,h2)
'''
'''
pyautogui.alert(title='请一定仔细阅读',button='ok',text="""请先阅读\n1,运行本程序时鼠标被独占!其他工作不能进行,请空闲时运行!\n停止运行本程序方法:将鼠标快速移动到屏幕一角,并停留5秒\n
2,使浏览器最大化或至少使浏览器上下满屏;播放视频,将视频播放窗口全部显示于浏览器中,不要被广告或其他程序遮挡\n
3,本程序只有答题功能和自动播放下一小节功能\n
4,我用QQ浏览器没问题,有问题再说\n
                      2022.2.21
""")
s=pyautogui.prompt(title='请输入',text='从本课的第几小节开始学习?请输入',default=1)
n=int(s)
xiaojie(n)

try:
    for ww in range(36000):
        time.sleep(5)
        px,py=pyautogui.locateCenterOnScreen('end.png',confidence=0.9)
        pyautogui.moveTo(px,py-50)
        if pyautogui.locateCenterOnScreen('1.png',confidence=0.7):
            dianji()
        if pyautogui.locateCenterOnScreen('2.png') :
            n+=1
            xiaojie(n)
except:
    pyautogui.alert(title='程序退出',text='视频下部被遮挡或程序异常,程序退出,请手动学习\n或调整视频窗口后重新运行本程序!')


'''


















