import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunpro.items import SunproItem,NeirongItem,ImgItem

'''项目需求：题目、来源，详情页的作者、内容
'''
class SunSpider(CrawlSpider):
    name = 'sun'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.vdfly.com/movie/yingp/index.html']

    #链接提取器 allow='正则表达式'
    link_neirong = LinkExtractor(allow=r'/movie/\d+/\d+\.html')
    link=LinkExtractor(allow=r'/yingp/\d+\.html')

    #规则解析器
    rules = (
        Rule(link, callback='parse_item',follow=False),
        Rule(link_neirong,callback='parse_neirong')
    )

    def parse_item(self, response):
        #print(response)
        li_list=response.xpath('//*[@id="subPage"]/div[1]/div[1]/ul/li')
        #print(li_list)
        for li in li_list:
            timu=li.xpath('./div/a/text()')[0].extract()
            riqi=li.xpath('./div[2]/text()')[0].extract()
            item=SunproItem()
            item['timu']=timu
            item['riqi']=riqi
            yield item


    def parse_neirong(self,response):
        zhuozhe=response.xpath('//*[@id="main"]/div[1]/div[2]/span[3]/strong/text()')[0].extract()
        neirong=response.xpath('//*[@id="main"]/div[1]/div[4]//text()').extract()
        neirong=''.join(neirong)

        item=NeirongItem()
        item['zhuozhe']=zhuozhe
        item['neirong']=neirong
        yield item
        src = response.xpath('//*[@id="main"]/div[1]/div[4]//img/@src').extract()
        for imm in src:
            item = ImgItem()
            item['imm']=imm
            yield item


