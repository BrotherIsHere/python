import os

import requests
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/587.36 (KHTML, like Gecko) Chrome/97.0.4632.99 Safari/531.36'}


# 建立一个函数以后调运
def gethtml_text(url):
    try:
        response = requests.get(url=url, headers=headers, timeout=(115, 115))
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        print('连接异常')

"""
# 获取网页列表并生成字典
dicall={}
for i in range(333):
    print('正在下载第{}页----------'.format(i+1))
    url='https://jajibot.com/2048/thread.php?fid-18-page-{}.html'.format(i+1)
    tree=etree.HTML(gethtml_text(url))
    nalist=tree.xpath('//td[@class="tal"]/a//text()')
    naurl=tree.xpath('//td[@class="tal"]/a/@href')
    urllist = []
    for ur in naurl:
        urllist.append('https://jajibot.com/2048/'+ur)
    diclist=dict(zip(nalist,urllist))
    dicall=dict(dicall,**diclist)
    print(diclist)
    print('－－－－－－－－第{}页下载完成'.format(i+1))

with open('2048sjxz.txt','w',encoding='utf-8') as fp:
    fp.write(str(dicall)) 
"""


# 读取本地文件中的内容并转为字典
with open('2048sjxz.txt', 'r', encoding='utf-8') as dic1:
    dic2 =eval(dic1.read())
# 查找字典中的关键字并处理保存为文本
keyname = input('请输入关键字以搜索：')
fp = open('findok.txt', 'w', encoding='utf-8')
n = 1
for ss in dic2.keys():
    if keyname in ss:
        print('第{}条'.format(n))
        print(ss)
        print(dic2[ss])
        fp.write('第{}条'.format(n) + ss + '\n')
        fp.write(dic2[ss] + '\n')
        n+=1
"""        
#下载对应图片
        url = dic2[ss]
        u_text = requests.get(url=url, timeout=15, headers=headers).text
        tree1 = etree.HTML(u_text)
        imglist = tree1.xpath('//div[@class="tpc_content"]//img/@src')
        # print(imglist)
        dirlist = 'c:\\248\\a\\{}'.format(n)
        if not os.path.exists(dirlist):
            os.makedirs(dirlist)  # 创建多级文件夹用makedirs,一个用mkdir
        for img in imglist:
            try:
                rjpg = requests.get(url=img, headers=headers).content
            except:
                print('(---------------------------下载失败)')
                continue

            # with open(dirlist+'/'+img[-5:],'wb') as fimg:
            # with open(dirlist+'/'+img[-15:].rplace('/','333'),'wb') as fimg:#替换字符串用replace
            with open(dirlist + '/' + img.split('/')[-1], 'wb') as fimg:  # 用/分割字符串取最后一个字符串,例如2/23/4.jpg
                fimg.write(rjpg)

        n += 1
"""