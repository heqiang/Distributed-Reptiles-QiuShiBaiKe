# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from qiushibaike.items import QiushibaikeItem


class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['baike.com']
    host=""
    headers={
        "USER_AGENT": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    def start_requests(self):

        urls = 'https://www.qiushibaike.com/hot/'
        yield Request(urls,headers=self.headers)


    def parse(self, response):
        str=""
        item=QiushibaikeItem()
        for  qiushi in response.xpath('//div[@class="content-block clearfix"]/div[@id="content-left"]/div'):
            if len(qiushi.xpath('.//div[@class="author clearfix"]/a[2]/h2/text()')) is 0:
                item['author']="匿名用户"
            else:
                a=[x.strip() for x in qiushi.xpath('.//div[@class="author clearfix"]/a[2]/h2/text()').extract()]
                b=[x.strip() for x in qiushi.xpath('.//a/div[@class="content"]/span/text()').extract()]
                c=[x.strip() for x in qiushi.xpath('.//div[@class="stats"]/span[1]//text()').getall()]
                d=[x.strip() for x in qiushi.xpath('.//div[@class="stats"]/span[2]/a//text()').getall()]
                item['author']=str.join(a)
                item['content']=str.join(b)
                item['fullName']=str.join(c)
                item['sum_comment']=str.join(d)
                yield item
        next_page = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract()
        if next_page:
            next_page='https://www.qiushibaike.com'+next_page[0]
            yield Request(next_page,headers=self.headers,callback=self.parse,dont_filter=True)

