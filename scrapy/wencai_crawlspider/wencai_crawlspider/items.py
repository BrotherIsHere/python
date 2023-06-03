# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WencaiCrawlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    jianjie = scrapy.Field()

#在爬虫文件中不能有两个item,所以这要再建一个item
class ContentItem(scrapy.Item):
    content = scrapy.Field()
    title = scrapy.Field()