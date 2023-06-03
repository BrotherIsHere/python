# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import redis
import time
"""除了process_item()必须实现，管道类还有其它的方法实现:
1.open_spider(spider)
在Spider开启时被调用，主要做一些初始化操作，如连接数据库等。参数是即被开启的Spider对象
2.close_spider(spider)
在Spider关闭时被调用，主要做一些如关闭数据库连接等收尾性质的工作。参数spider就是被关闭的Spider对象
3.from_crawler(cls,crawler)
类方法，用@classmethod标识，是一种依赖注入的方式。它的参数是crawler，通过crawler对象，我们可以拿到Scrapy的所有核心组件，如全局配置的每个信息，然后创建一个Pipeline实例。参数cls就是Class，最后返回一个Class实例。
"""


class TpzjPipeline:
    #增加一个方法,使文件只在使用时打开一次
    fp=None
    def open_spider(self, spider):
        print("开始爬虫.......")
        self.fp=open("./tupian.txt","w",encoding="utf-8")

    def process_item(self, item, spider):
        name=item['name']
        content = item['content']
        # with open() #弃用,加为每调用一次item,文件就打开关闭一次
        self.fp.write(name+":"+str(content)+'\n')
        return item

    #增加一个关闭文件的方法
    def close_spider(self,spider):
        print("爬虫结束")
        self.fp.close()

#管道文件中的一个管道只能将数据存储到一个平台或载体,若存储到其它载体或平台,需再建一个类
#将数据存储到redis中
class RedisPipeline(object):  #仿制一个类
    #建立redis连接池

    def open_spider(self,spider):
        print('开始redis')
    pool=redis.ConnectionPool(host="192.168.188.100",port=6379,decode_responses=True)
    r=redis.Redis(connection_pool=pool)

    #处理item
    def process_item(self, item, spider): # 仿制一个方法
        name=item['name']
        content=item["content"]
        self.r.rpush("tpzj",name+":"+str(content)+"\n")
        #print(self.r.llen("tpzj"))
        return item

    def close_spider(self,spider):
        print("redis结束")


