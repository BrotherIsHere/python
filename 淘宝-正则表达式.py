#整体框架

import requests
import re

#获得页面的函数
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('连接异常')
        return ''

#对页面进行解析
def parsePage(ilt,html):#ilt结果的列表类型，html页面的信息
    print("")

#淘宝的商品信息输出到页面上
def printGoodslist(ilt):
    print("")

#定义一个主函数来记录整个程序运行过程
def main():
    goods='书包' #搜索的关键词
    depth=2 #爬取的深度
    #淘宝爬取的相关url
    start_url='http://s.taobao.com/search?q='+goods
    infolist=[] #整个的输出结果
    for i in range(depth):
        try:
            #每个页面的完整url
            url=start_url+'&s='+str(44*i)
            #获取页面内容
            html=getHTMLText(url)
            #解析页面内容获得输出结果
            parsePage(infolist,html)
        except:
            continue
    #打印输出结果
    printGoodslist(infolist)

main()


