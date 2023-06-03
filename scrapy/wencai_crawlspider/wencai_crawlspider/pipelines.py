# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WencaiCrawlspiderPipeline:
    def process_item(self, item, spider):
        # 将列表页内容和内容页内容分别提取,如果一块提取两个item不同时出现会出错如:
        #print(item['name'],item['jianjie'],item['content'])
        if item.__class__.__name__=="WencaiCrawlspiderItem":
            print(item["name"],item['jianjie'])
        else:
            print(item["title"],item['content'])


        return item
