import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wencai_crawlspider.items import WencaiCrawlspiderItem
from wencai_crawlspider.items import ContentItem

""" 利用crawlspider进行全站爬取
scrapy genspider -t crawl wencai www.wencaidao.com"""
#爬取标题,简介,内容(在不同页)
class WencaiSpider(CrawlSpider):
    name = 'wencai'
    #allowed_domains = ['www.wencaidao.com']
    start_urls = ['http://www.wencaidao.com/']

    """规则解析器=(链接提取器,解析函数回调, 在链接页继续提取链接=False True )
    """
    #链接提取器,根据规则进取指定页链接
    link=LinkExtractor(allow=r'http://www\.wencaidao\.com/[a-z]+_?\d*\.html')
    #内容页链接提取
    link_content=LinkExtractor(allow=r"http://www\.wencaidao\.com/page/file\d+/\d+\.html")
    #规则解析器,将链接提取器提取的链接进行指定规则的解析
    rules = (
        Rule(link, callback='parse_item', follow=False),
        Rule(link_content, callback='parse_content', follow=False),
    )
    #以下不能请示传参,要存到两个item中
    def parse_item(self, response):
        li_list=response.xpath("//*[@id=\"app\"]/section[2]/div/div[2]/ul/li")
        for li in li_list:
            name=li.xpath("./span/h3/a/text()").extract_first()
            jianjie=li.xpath("./span/p/text()").extract_first()

            item = WencaiCrawlspiderItem()
            item['name']=name
            item['jianjie']=jianjie
            yield item
    def parse_content(self, response):
        title=response.xpath('//*[@id="app"]/article/div/div/div[1]/div/h1/text()').extract_first()
        content=response.xpath('//*[@id="app"]/article/div/div/div[1]/div/h2/time/text()').extract_first()
        item=ContentItem()
        item['content'] = content
        item['title'] = title
        yield item