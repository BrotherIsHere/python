import scrapy


class TupianzjSpider(scrapy.Spider):
    name = 'tupianzj'
    #allowed_domains = ['www.tupianzj.com']
    start_urls = ['https://www.tupianzj.com/meinv/xinggan/list_176_1.html']

    num=2
    def li_parse(self,response):

        nums=response.xpath('//*[@id="container"]/div/div/div[2]/div[2]/div[3]/ul/li[1]/a/text()')[0].extract()[1:-3]
        print(nums)
        neirong=response.xpath('//*[@id="bigpicimg"]/@src')[0].extract()
        print(neirong)
        li_url = response.meta['li_url']
        print(li_url)
        #if self.num <= int(nums):
            #print(self.li_url[0:-5] + '_{}.html'.format(self.num))
            #yield scrapy.Request(self.li_url[0:-5]+'_{}.html'.format(self.num),callback=self.li_parse)
            #self.num += 1




        # except:
        #     #neirong=response.xpath('//*[@id="container"]/div/div/div[2]/div[2]/div[1]/div[2]/div/div/img/@src | //*[@id="bigpicimg"]/@src')[0].extract()
        #     #print(neirong)
        #     print(999)




    def parse(self, response):
        #第一页xgmn索引页:
        li_list=response.xpath('//*[@id="container"]/div/div/div[3]/div/ul/li')
        #print(li_list)
        for li in li_list:
            self.li_url='https://www.tupianzj.com'+li.xpath('./a/@href')[0].extract()
            #print(li_url)
            yield scrapy.Request(self.li_url,callback=self.li_parse)

        pass
