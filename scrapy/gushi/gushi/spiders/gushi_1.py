import scrapy
from gushi.items import GushiItem
import redis

class Gushi1Spider(scrapy.Spider):
    name = 'gushi_1'
    #allowed_domains = ['www.gushi.com']
    start_urls = ['http://www.wencaidao.com/gushi.html']
    num = 1
    url="http://www.wencaidao.com/gushi_{}.html"
    # pool=redis.ConnectionPool(host="192.168.188.100",port=6379,decode_responses=True)
    # r=redis.Redis(connection_pool=pool)

    def parse(self, response):
        content_list = response.xpath('//*[@id="app"]/section[2]/div/div[2]/ul/li')
        for bc in content_list:
            bi = bc.xpath('./span/h3/a/text()').extract_first()
            content = bc.xpath('./span/p/text()').extract_first()
            # print(type(bi))
            # print(type(content))
            # self.r.rpush("gushi1",bi,str(content))
            item=GushiItem()
            item["bi"]=bi
            item["content"]=content

            yield item
        if self.num<3:
            self.num+=1
            new_url=self.url.format(self.num)
            yield scrapy.Request(url=new_url,callback=self.parse)


