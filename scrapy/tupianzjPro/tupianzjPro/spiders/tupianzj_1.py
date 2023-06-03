import scrapy


class Tupianzj1Spider(scrapy.Spider):
    name = 'tupianzj_1'
    #allowed_domains = ['www.sss.com']
    start_urls = ['https://www.tupianzj.com/meinv/20220208/237762.html']

    num=2
    def parse(self, response):
        nums=response.xpath('//*[@id="container"]/div/div/div[2]/div[2]/div[3]/ul/li[1]/a/text()')[0].extract()[1:-3]
        img=response.xpath('//*[@id="bigpicimg"]/@src')[0].extract()
        print(img)
        if self.num <= int(nums):
            yield scrapy.Request(self.start_urls[0][0:-5]+'_{}.html'.format(self.num),callback=self.parse)
            self.num+=1

