import base64
'''
def pic2py(picname):
    pic_read=open(picname,'rb')
    pic_64=base64.b64encode(pic_read.read())
    pic_read.close()

    pic_py=open(picname.replace('.','_')+'.py','w')
    write_data='img="{}"'.format(pic_64.decode())
    pic_py.write(write_data)
    pic_py.close()

png_list=['bofang.png','kechengzj.png','red.png','wenti.png']
for i in png_list:
    pic2py(i)
'''

from bofang_png import img as bofang
from kechengzj_png import img as kechengzj
from red_png import img as red1
from wenti_png import img as wenti

pic_w=open('wenti.png','wb')
write_data=base64.b64decode(wenti)
pic_w.write(write_data)
pic_w.close()

pic_w=open('red.png','wb')
write_data=base64.b64decode(red1)
pic_w.write(write_data)
pic_w.close()

pic_w=open('bofang.png','wb')
write_data=base64.b64decode(bofang)
pic_w.write(write_data)
pic_w.close()

pic_w=open('kechengzj.png','wb')
write_data=base64.b64decode(kechengzj)
pic_w.write(write_data)
pic_w.close()


