import pyautogui
import time
import base64


'''
#因为installer不能打包图片
#将图片转为py文件的函数
def pic2py(picname):
    pic_read=open(picname,'rb')
    #将读取人图片二进制内容转化为base64编码
    pic_64=base64.b64encode(pic_read.read())
    pic_read.close()

    pic_py=open(picname.replace('.','_')+'.py','w')
    #将编码后的base64内容写入py文件
    #注意加.decode
    write_data='img="{}"'.format(pic_64.decode())#注意加.decode
    pic_py.write(write_data)
    pic_py.close()
#利用函数将多个图片转为py文件
png_list=['bofang.png','kechengzj.png','red.png','wenti.png']
for i in png_list:
    pic2py(i)


#将py文件转为图片并开始使用
from bofang_png import img as bofang
from kechengzj_png import img as kechengzj
from red_png import img as red1
from wenti_png import img as wenti

pic_w=open('./img/wenti.png','wb')
write_data=base64.b64decode(wenti)
pic_w.write(write_data)
pic_w.close()

pic_w=open('./img/red.png','wb')
write_data=base64.b64decode(red1)
pic_w.write(write_data)
pic_w.close()

pic_w=open('./img/bofang.png','wb')
write_data=base64.b64decode(bofang)
pic_w.write(write_data)
pic_w.close()

pic_w=open('./img/kechengzj.png','wb')
write_data=base64.b64decode(kechengzj)
pic_w.write(write_data)
pic_w.close()
'''

#点击播放第n节课
def xiaojie(n):
    try:
        dd = pyautogui.locateCenterOnScreen(r'.\img\red.png')
        pyautogui.doubleClick(dd)
        pyautogui.scroll(-700)
        time.sleep(1)
        kx,ky=pyautogui.locateCenterOnScreen(r'.\img\kechengzj.png')
        kx2,ky2=kx-300,ky+45+50*(n-1)
        pyautogui.doubleClick(kx2,ky2)
        time.sleep(1)
        pyautogui.scroll(-600)
    except:
        pyautogui.alert(title='????', text='视频窗口位置异常?,调整到中央!')
        time.sleep(8)

#自动答题函数,鼠标在一定范围内点击
def dianji():
    #查找问题图像并点击
    w1,h1=pyautogui.locateCenterOnScreen(r'.\img\wenti.png')
    h1+=40
    for hj in range(15):
        h2=h1+20*hj
        for wj in range(10):
            w2=w1+20*wj
            pyautogui.click(w2,h2)


#程序从这里开始运行
#弹出确认框
pyautogui.alert(title='请一定仔细阅读',button='ok',text='''请先阅读\n1,运行本程序时鼠标被独占!其他工作不能进行,请空闲时运行!\n停止运行本程序方法:将鼠标快速移动到屏幕一角,并停留5秒\n
2,使浏览器最大化或至少使浏览器上下满屏;播放视频,将视频播放窗口全部显示于浏览器中,不要被广告或其他程序遮挡\n
3,本程序只有答题功能和自动播放下一小节功能\n
4,我用QQ浏览器没问题,有问题再说\n
                      2022.2.21
''')

#弹出提示框,运行第n节
s=pyautogui.prompt(title='请输入',text='从本课的第几小节开始学习?请输入',default=1)
n=int(s)
xiaojie(n)

try:
    for ww in range(36000):#重复执行下列函数
        time.sleep(1)
        px,py=pyautogui.locateCenterOnScreen(r'.\img\red.png')
        pyautogui.moveTo(px,py-50)
        if pyautogui.locateCenterOnScreen(r'.\img\wenti.png'):
            dianji()
        if pyautogui.locateCenterOnScreen(r'.\img\bofang.png') :
            n+=1
            xiaojie(n)
except:
    pyautogui.alert(title='程序退出',text='视频下部被遮挡或程序异常,程序退出,请手动学习\n或调整视频窗口后重新运行本程序!')



