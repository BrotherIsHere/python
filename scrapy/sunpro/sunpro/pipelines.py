# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SunproPipeline:
    def process_item(self, item, spider):
        if item.__class__.__name__=='NeirongItem':
            print(item['zhuozhe'],item['neirong'])
        elif item.__class__.__name__=='SunproItem':
            print(item['timu'],item['riqi'])

        return item
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class Img(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['imm'])

    def file_path(self, request, response=None, info=None, *, item=None):
        img_name=request.url.split('/')[-1]
        return img_name
    def item_completed(self, results, item, info):
        return item
