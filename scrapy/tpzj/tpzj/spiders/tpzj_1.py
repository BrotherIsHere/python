import scrapy
from tpzj.items import TpzjItem


class Tpzj1Spider(scrapy.Spider):
    name = 'tpzj_1'
    #allowed_domains = ['www.tupianzj.com']
    start_urls = ['http://www.wencaidao.com/gushi.html']

    def parse(self, response):
        #print(response.text)
        tp_list = response.xpath("//*[@id=\"app\"]/section[2]/div/div/ul/li/span")
        #t_list=[]
        #dic={}
        #n=0
        for i in tp_list:
            name=i.xpath("./h3/a/text()").extract_first()
            # print(name)
            content=i.xpath("./p/text()").extract()
            content=''.join(content)
            # print(content)
            # dic = {}
            # dic["name"] = name
            # dic["content"] = content
            # t_list.append(dic)
            # print(t_list)
            # n+=1
            # if n==5 :
            #     break
            item = TpzjItem()
            item['name']=name
            item["content"]=content
            yield item


        # print(response.url)
        # print(response.request.url)
        # print(response.headers)
        # print(response.request.headers)
