# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import redis

class GushiPipeline:
    # pool=redis.ConnectionPool(host="192.168.188.100",port=6379,decode_responses=True)
    # r=redis.Redis(connection_pool=pool)
    fp=None
    def open_spider(self,spider):
        print("打开text文件,开始写入.....")
        self.fp=open("gushi.txt",'w',encoding="utf-8")
    def process_item(self, item, spider):
        bi=item['bi']
        content=item["content"]
        #print(biaoti,content)
        self.fp.write(bi+':'+str(content))
        # self.r.rpush("gushi",bi+":"+str(content))
        return item

    def close_spider(self,spider):
        print(" 写入完成......")
        self.fp.close()



