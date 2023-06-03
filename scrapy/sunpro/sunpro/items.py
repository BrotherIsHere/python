# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    timu = scrapy.Field()
    riqi = scrapy.Field()

class NeirongItem(scrapy.Item):
    zhuozhe = scrapy.Field()
    neirong = scrapy.Field()

class ImgItem(scrapy.Item):
    imm = scrapy.Field()

