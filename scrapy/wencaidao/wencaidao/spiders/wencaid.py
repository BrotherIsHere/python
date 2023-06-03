import copy
import scrapy
from wencaidao.items import WencaidaoItem

'''
采集全网,主页,栏目,标题,内容
'''
class WencaidSpider(scrapy.Spider):
    name = 'wencaid'
    #allowed_domains = ['www.wencaidao.com']
    start_urls = ['http://www.wencaidao.com/'] # 起始页
    url_add="http://www.wencaidao.com/" # 补充url

    # 函数回调,采集内容页面,
    def parse_content(self, response):
        # 请求传参,此时item已经包含前面的内容,后面可一同yield
        item = response.meta["item"] #提取前面的item字典
        #解析内容
        content = response.xpath('//*[@id="app"]/article/div/div/div[1]/div/h2/time/text()').extract_first()
        #将内容加入item字典中
        item["content"] = str(content)
        yield item #将item交给管道

    #处理主页
    def parse(self, response):
        #获取li元素
        li_list=response.xpath('//*[@id="app"]/section[2]/div/div/ul/li')
        #获取栏目元素
        lanmu_list=response.xpath('//*[@id="app"]/nav/div/ul/li')
        item=WencaidaoItem() #调入item类

        #获取标题,内容url,简介
        for li in li_list:
            content_url=li.xpath("./span/h3/a/@href").extract_first() #内容页url
            title=li.xpath("./span/h3/a/text()").extract_first() # 标题
            jianjie=li.xpath('./span/p/text()').extract_first() # 简介
            # 将内容页url,标题,简介封装到item字典
            item["title"] = str(title)
            item['jianjie'] = str(jianjie)
            item['content_url'] = content_url
            # print(title+content_url+jianjie+"\n")
            # 注意,请求传参时meta={"item":item}是浅复制会出错,用meta={"item":copy.deepcopy(item)}
            yield scrapy.Request(url=content_url,callback=self.parse_content,meta={"item":copy.deepcopy(item)}) # 传参item(请求传参)

        #本栏目1.2.3...分页采集
        #获取分页列表
        page_num = response.xpath('//*[@id="app"]/section[2]/div/div[1]/h3/a/@href').extract()
        #获取期中一页面
        for p in page_num:
            #print(p)
            #函数回调,采集本栏目的下一页
            yield scrapy.Request(url=p,callback=self.parse) # 递归函数

        # #获取各个栏目内容
        for lan in lanmu_list:
            lan_name=lan.xpath('./a/text()').extract_first() #栏目名称
            lan_url=lan.xpath('./a/@href').extract_first() #栏目url

            #函数回调,获取下一栏目
            try: #如果url不完整出错 ,则采用补加
                yield scrapy.Request(url=lan_url,callback=self.parse)
            except:
                yield scrapy.Request(url=self.url_add+lan_url, callback=self.parse) # 递归函数



