import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meinvpro.items import MeinvproItem

class MeinvSpider(CrawlSpider):
    name = 'meinv'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wencaidao.com/gushi.html']

    rules = (
        #Rule(LinkExtractor(allow=r'/meinv/\d+/\d+\.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'state/p/24/22\d{2}/\d+\.html'),callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/thread\.php\?fid-24-page-\d{1,2}\.html'), follow=True),

    )

    def parse_item(self, response):
        try:
            pics=response.xpath('//*[@id="read_tpc"]//img/@src').extract()
            for pic in pics:
                item=MeinvproItem()
                item['pic']=pic
                yield item
        except:
            pass

