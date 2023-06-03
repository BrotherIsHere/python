import requests
import os
from lxml import etree

url='https://tm.1314cai.com/2048/thread.php?fid-277-page-2.html'
headers= {

    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
response=requests.get(url=url,headers=headers)
r_text=response.text
tree=etree.HTML(r_text)
list_text=tree.xpath('//tr[@align="center"]/td[@class="tal"]/a[1]/@href')

for i in list_text:
    ii='https://tm.1314cai.com/2048/'+i
    #print(ii)
    pic_text=requests.get(url=ii,headers=headers).text
    pictree=etree.HTML(pic_text)
    piclist=pictree.xpath('//img/@src')
    #print(piclist)
    for pi in piclist:
        if '.jpg' in pi:
            print(pi)
            img=requests.get(pi).content
            dirlist='c:/a/pic/'
            if not os.path.exists(dirlist):
                os.makedirs(dirlist)
            with open(dirlist+pi.split('/')[-1],'wb') as fp:
                fp.write(img)



