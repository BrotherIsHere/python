# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class YingproPipeline:
#     def process_item(self, item, spider):
#         return item
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class Imgpipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img'])
    def file_path(self, request, response=None, info=None, *, item=None):
        filename=request.url.split('/')[-1]
        return filename
    def item_completed(self, results, item, info):
        return item
