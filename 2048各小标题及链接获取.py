import requests
from lxml import etree

def html_text(url):
    try:
        headers={'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
        response=requests.get(url=url,headers=headers)
        response.raise_for_status()
        response.encoding=response.apparent_encoding
        response_text=response.text
        return response_text
    except:
        print('网络连接异常')
i=1
d1={}
while i<=1543 :
    print('----------正在下载第{}页----------'.format(i))
    url='https://bbs.h871.com/2048/thread.php?fid-279-type-528-page-{}.html'.format(i)
    #print(html_text(url))
    tree=etree.HTML(html_text(url))
    htmllisturl=tree.xpath('//h3/a/@href')
    urllist=[]
    for ur in htmllisturl:
        url1='https://bbs.h871.com/2048/'+ur
        urllist.append(url1)
    htmllistname=tree.xpath('//h3/a/text()')
    hao=dict(zip(htmllistname,urllist))
    d1=dict(d1,**hao)

    print('--------第{}页完成----------'.format(i))
    i+=1
with open('2048list.txt','w',encoding='utf-8') as fp:
    fp.write(str(d1))
