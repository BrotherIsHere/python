#Umei.cc网站下载图片
import requests
from lxml import etree
import os
from bs4 import BeautifulSoup

url='https://umei.cc/meinvtupian/meinvxiezhen/'
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
response=requests.get(url=url,headers=headers)
response.encoding='utf-8'
page_text=response.text
#print(page_text)
tree=etree.HTML(page_text)
li_list=tree.xpath('//div[@class="TypeList"]//a/@href')
#print(li_list)
if not os.path.exists('./Umei'):
    os.mkdir('./Umei')
n=1
for li in li_list:
    li_url = 'https://umei.cc' + li
    while True:

        #print(li_url)
        lli=requests.get(url=li_url,headers=headers)
        lli.encoding='utf-8'
        lli_text=lli.text
        #print(lli_text)
        lli_tree=etree.HTML(lli_text)
        jpg_dizhi=lli_tree.xpath('//div[@class="ImageBody"]//img/@src')[0]
        #print(jpg_dizhi)
        with open('Umei/'+str(n)+'.jpg','wb') as fp:
            ll_pic=requests.get(url=jpg_dizhi,headers=headers).content
            fp.write(ll_pic)
            print(jpg_dizhi,li_url)
            n+=1
            li_url = 'https://umei.cc' + lli_tree.xpath('//div[@class="ImageBody"]//a/@href')[0]

        if "?" in li_url:
            break


