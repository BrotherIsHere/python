import requests
from lxml import etree
import os
shu=2
n=1

while True:
    url='https://up.my4qbc.live/2048/thread.php?fid-23-page-{}.html'.format(str(shu))
    print(url)
    headers={'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    response=requests.get(url=url,headers=headers)
    response.encoding='utf-8'
    page_text=response.text
    #print(page_text)
    tree=etree.HTML(page_text)
    html_list=tree.xpath('//td[@class="tal"]/a/@href')
    #print(html_list)

    ye=1
    for page in html_list:
        page_url='https://up.my4qbc.live/2048/'+page
        print(page_url+'  is page '+str(ye))
        ye+=1
        r_page=requests.get(url=page_url,headers=headers)
        r_page.encoding="utf-8"
        r_text=r_page.text
        #print(r_text)
        rtree=etree.HTML(r_text)
        pic_list=rtree.xpath('//ignore_js_op[@class="att_img"]/img/@src')
        #print(pic_list)
        if not os.path.exists('./248pic'):
            os.mkdir('./248pic')
        try:
            for pi in pic_list:
                picpath='248pic/'+str(n)+'.jpg'
                pic=requests.get(url=pi,headers=headers).content
                with open(picpath,'wb') as fp:
                    fp.write(pic)
                    print(pi+'下载成功！',end='')
                    print(n)
                    n+=1
        except ConnectionResetError as ss:
            print(ss)
            break
    shu+=1