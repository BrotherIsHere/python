import scrapy


class XiutuSpider(scrapy.Spider):
    name = 'xiutu'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://xiaohua.zol.com.cn/gedifangyan/']

    def parse(self, response):
        pass
