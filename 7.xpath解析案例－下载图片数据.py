import requests
from lxml import etree
import os

'''if __name__=='__main__':
    try:
        url='https://pic.netbian.com/4kmeinv/'
        headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
        response=requests.get(url=url,headers=headers)
        response.raise_for_status()
        response.encoding=response.apparent_encoding
        response_text=response.text
        print(response_text)
    except:
        print('网络连接异常')'''

import requests
from lxml import etree
import os
if __name__=='__main__':
    url='https://pic.netbian.com/4kmeinv/'
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    response=requests.get(url=url,headers=headers)
    #可以手动修改响应数据的编码格式
    #response.encoding='gbk'
    page_text=response.text
    print(page_text)

    tree=etree.HTML(page_text)
    list_li=tree.xpath('//div[@class="slist"]//li')
    print(list_li)
    #创建一个文件夹
    if not os.path.exists('./piclibs'):
        os.mkdir('./piclibs')

    for li in list_li:
        img_src='https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
        #通用处理中文乱码的方法(注意重新赋值）
        img_name=img_name.encode('iso-8859-1').decode('gbk')
        #print(img_name,img_src)
        #请求图片进行持久存储
        img_data=requests.get(url=img_src,headers=headers).content
        img_path='piclibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功!')
