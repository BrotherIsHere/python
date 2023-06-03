# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WencaidaoPipeline:

    fp=None
    def open_spider(self,spider):
        self.fp=open('wendao.txt','w',encoding='utf-8')
    def process_item(self, item, spider):

        title=item["title"]
        jianjie=item['jianjie']
        content=item['content']
        content_url=item['content_url']

        #print(title,content_url,jianjie,content)
        self.fp.write(title+":"+content_url+jianjie+content+"\n")
        return item
    def close_spider(self,spider):
        self.fp.close()