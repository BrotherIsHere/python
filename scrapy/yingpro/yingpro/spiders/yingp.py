import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yingpro.items import YingproItem


class YingpSpider(CrawlSpider):
    name = 'yingp'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.vdfly.com/movie/yingp/index.html']

    rules = (
        Rule(LinkExtractor(allow=r'/movie/\d+/\d+\.html'), callback='parse_item',follow=False),
        Rule(LinkExtractor(allow=r'/movie/yingp/\d+\.html'),  follow=False),

    )

    def parse_item(self, response):
        img_list=response.xpath('//*[@id="main"]/div[1]/div[4]//img/@src').extract()
        for img in img_list:
            item=YingproItem()
            item['img']=img
            yield item
